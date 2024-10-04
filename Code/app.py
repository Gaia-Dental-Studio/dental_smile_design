import streamlit as st
import PIL
import settings
import helper
import os
import cv2
import requests
import subprocess
import time
from io import BytesIO
# from streamlit_modal import Modal

st.set_page_config(
    page_title="Tooth Aligner",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Tooth Aligner")

# Sidebar
st.sidebar.header("ML Model Config")

upload_dir = "../Data"
output_dir = "../Output/prediction"
source_path = None
model_args = None

source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
# col1, col2 = st.columns(2)

# model_args = helper.loadModelConfig()
# modal = Modal("Enter your email to send the result", key="demo-modal")


# with col1:
if source_img is not None:
    # Save the uploaded image to the 'uploads' directory
        image_path = os.path.join(upload_dir, source_img.name)
        with open(image_path, "wb") as f:
            f.write(source_img.getbuffer())

        # Display the uploaded image
        st.image(image_path, caption="Uploaded Image", use_column_width=True)
        st.write("Image uploaded successfully!")

        if st.button("Transform"):
        # Construct the command: "python main.py -i <image_path>"
            command = f"python main.py -i {image_path}"
            st.write(f"Running command: {command}")
        
            try:
                # Use subprocess to run the command
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                st.write(result.stdout.decode("utf-8"))  # Display command output

                # Wait for the transformed image to be generated
                output_image_name = source_img.name.split('.')[0] + ".png"  # Assuming output is saved as .png
                output_image_path = os.path.join(output_dir, output_image_name)

                # Wait for the file to be generated (you might need to adjust sleep duration)
                while not os.path.exists(output_image_path):
                    time.sleep(1)  # Wait 1 second before checking again
                
                # Display the transformed image
                st.image(output_image_path, caption="Transformed Image", use_column_width=True)
                st.success("Transformation completed successfully!")
            
            except subprocess.CalledProcessError as e:
                st.error(f"Error occurred while running the transformation: {e.stderr.decode('utf-8')}")



#     try:
#         if source_img is None:
#             default_image_path = str(settings.DEFAULT_IMAGE)
#             default_image = PIL.Image.open(default_image_path)
#             st.image(default_image_path, caption="Default Image",
#                         use_column_width=True)
#         else:
#             uploaded_image = PIL.Image.open(source_img)
#             # cv2.imwrite(os.path.join(os.path.join(model_args.out_path, 'prediction'), img_name+'.png'), pred_face)
#             uploaded_image.save(os.path.join('../Data',source_img.name))
#             source_path = '../Data/' + source_img.name
#             st.image(source_img, caption="Uploaded Image",
#                         use_column_width=True)
#     except Exception as ex:
#         st.error("Error occurred while opening the image.")
#         st.error(ex)


# with col2:
#         if source_img is None:
#             default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
#             default_detected_image = PIL.Image.open(
#                 default_detected_image_path)
#             st.image(default_detected_image_path, caption='Detected Image',
#                      use_column_width=True)
#         else:
#             if st.sidebar.button('Detect Objects'):
                
                
#                 # api_url = 'http://127.0.0.1:5000/'
#                 # files = {'img': open(source_path, 'rb')}
#                 # response_post = requests.post(api_url + 'object-detection', files=files)
#                 # image_data=response_post.content
#                 # print(image_data)

#                 output_path = "../Output/prediction/"
#                 img_file = PIL.Image.open(output_path)
#                 st.image(img_file,caption="Result Image")
                
      
