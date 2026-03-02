import cv2
import streamlit as st
import yaml
import os
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="Frog Pipeline - ROI Setup", layout="wide")

# st.markdown(
#     """
#     <style>
#     /* Invert Canvas Icons (Undo, Redo, Trash) to be visible on dark background */
#     button[title="Undo"], button[title="Redo"], button[title="Reset"], button[title="Trash"] {
#         filter: invert(100%) brightness(200%);
#     }
#     /* Hide the 'Deploy' button and Streamlit header */
#     header {visibility: hidden;}
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     /* Clean dark background */
#     .stApp { background-color: #0e1117; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.title("Nursery ROI Configuration Tool")

ASSIGNMENT_RULES = {
    "variabilis": {
        "cup_1": "Parental",
        "cup_2": "Parental",
        "cup_3": "Control",
        "cup_4": "Parental"
    },
    "imitator": {
        "cup_1": "Parental",
        "cup_2": "Foster",
        "cup_3": "Control",
        "cup_4": "Foster"
    }
}

raw_base_path = "src/data/raw"
species_options = [d for d in os.listdir(raw_base_path) if os.path.isdir(os.path.join(raw_base_path, d))]

if not species_options:
    st.error(f"No species folders found in {raw_base_path}.")
else:
    selected_species = st.selectbox("Select Species", species_options)
    species_path = os.path.join(raw_base_path, selected_species)
    
    sessions = [d for d in os.listdir(species_path) if os.path.isdir(os.path.join(species_path, d))]
    
    if not sessions:
        st.warning(f"No session folders found in {species_path}.")
    else:
        selected_session = st.selectbox("Select Session Folder", sessions)
        video_dir = os.path.join(species_path, selected_session)
        video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi'))]
        
        if not video_files:
            st.warning(f"No videos found in {video_dir}.")
        else:
            selected_video = st.selectbox("Select Video for ROI Template", video_files)
            video_full_path = os.path.join(video_dir, selected_video)

            cap = cv2.VideoCapture(video_full_path)
            success, frame = cap.read()
            cap.release()

            if success:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                
                st.info(f"Drawing for **{selected_species}**. Order: Cup 1 (TL), 2 (TR), 3 (BL), 4 (BR).")

                canvas_result = st_canvas(
                    fill_color="rgba(255, 0, 255, 0.2)",
                    stroke_width=2,
                    stroke_color="#FF00FF",
                    background_image=img,
                    height=img.height,
                    width=img.width,
                    drawing_mode="rect",
                    key="canvas",
                    display_toolbar=True # We are keeping it but fixing icons via CSS
                )

                if canvas_result.json_data is not None:
                    objects = canvas_result.json_data["objects"]
                    if len(objects) == 4:
                        if st.button(f"Update Master {selected_species} Config"):
                            labels = ["cup_1", "cup_2", "cup_3", "cup_4"]
                            
                            # Construct the clean Dictionary
                            config_data = {
                                "species": selected_species,
                                "session_type": "fixed_camera",
                                "rois": {},
                                "assignments": ASSIGNMENT_RULES.get(selected_species, {})
                            }
                            
                            for i, obj in enumerate(objects):
                                # Save as [x1, y1, x2, y2]
                                config_data["rois"][labels[i]] = [
                                    int(obj["left"]), int(obj["top"]),
                                    int(obj["left"] + obj["width"]), int(obj["top"] + obj["height"])
                                ]
                            
                            os.makedirs("configs", exist_ok=True)
                            config_path = f"configs/species_{selected_species}.yaml"
                            
                            # Use default_flow_style=None to get the [ ] bracket format
                            with open(config_path, "w") as f:
                                yaml.dump(config_data, f, default_flow_style=None, sort_keys=False)
                                
                            st.success(f"Master config updated with correct formatting: {config_path}")
                    else:
                        st.warning(f"Please draw exactly 4 boxes. Currently: {len(objects)}")