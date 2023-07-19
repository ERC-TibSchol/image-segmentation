# Image Segmentation

These codes allow you to cut an input image into two or four equal horizontal segments and save them as separate images. They utilise the Python Imaging Library (PIL) to perform the image segmentation.

These scripts were created for the ERC project The Dawn of Tibetan Buddhist Scholasticism (11th-13th c.) (TibSchol). Cf. https://www.oeaw.ac.at/ikga/tibschol for more information.

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 101001002). See https://cordis.europa.eu/project/id/101001002.

# Functions
`cut_image_into_segments(image_path, output_folder)`: opens the image, divides it into two or four equal segments, saves each segment as a separate image file in the specified output folder, and prints the segment number and corresponding filename.

# Usage
1. Replace the `image_path` variable with the path to your input image
2. Replace the `output_folder` variable with the desired path for the output folder where the segmented images will be saved

# Notes 
The code assumes that the input image is in a common image format (e.g., JPEG, PNG). Adjust the image path and output folder path accordingly if you are working with a different image format or file structure.
