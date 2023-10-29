# Face Recognition and Verification

This Python script provides a simple command-line tool for comparing and verifying faces using two different methods: Face Recognition and DeepFace. It allows you to compare two face images and check whether they belong to the same person.

## Prerequisites

Before using this script, ensure that you have the necessary Python libraries installed. You can install the required packages using pip:
```
pip install face_recognition deepface
```

## Usage

1. Place the images you want to compare in the same directory as the script. The images should be in common formats like JPEG, PNG, or GIF.

2. Run the script using the following command:

```
pip install face_recognition deepface
```

3. The script will identify the faces in the provided images and verify whether they belong to the same person.

4. The results of the verification using two different methods, Face Recognition and DeepFace, will be displayed. You will see either "✔ - Verified" (if the faces match) or "❌ - Not Verified" (if the faces do not match).

5. You can choose to check again or exit the program by typing "again" or pressing "Enter" when prompted.

## Customization

You can customize the script to use different image files by modifying the `find_image_files` function. The function returns the paths of the first two image files it finds in the current directory. You can change the default file names or use your own images.


## Author

- vova9199

Feel free to contribute, report issues, or suggest improvements.

Happy face verification!
