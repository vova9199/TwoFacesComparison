import os

import face_recognition

from deepface import DeepFace


def check_face_recognition(image_of_person_1='1.jpg', image_of_person_2='2.jpg'):
    try:
        # Загрузите изображения
        image_of_person_1 = face_recognition.load_image_file(image_of_person_1)
        image_of_person_2 = face_recognition.load_image_file(image_of_person_2)

        # Получите кодировки (эмбеддинги) лиц на изображениях
        person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
        person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]

        # Сравните эмбеддинги для верификации
        results = face_recognition.compare_faces([person_1_face_encoding], person_2_face_encoding)

        if results[0]:
            result = "✔ - Verified"
        else:
            result = "❌ - Not Verified"
        return result

    except Exception as e:
        return f"Error: {e}"


def check_deepface(image_of_person_1='1.jpg', image_of_person_2='2.jpg'):
    try:
        # Выполните верификацию
        result = DeepFace.verify(image_of_person_1, image_of_person_2)

        if result["verified"]:
            result = "✔ - Verified"
        else:
            result = "❌ - Not Verified"
        return result

    except Exception as e:
        return f"Error: {e}"


def find_image_files():
    image_extensions = ['.png', '.jpeg', '.jpg', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.heic', '.raw', '.psd']
    image_files = [f for f in os.listdir() if
                   os.path.isfile(f) and any(f.lower().endswith(ext) for ext in image_extensions)]

    if image_files:
        return sorted(image_files)[:2]  # Возвращаем первые два файлы, если они существуют
    else:
        return ['1.jpg', '2.jpg']  # Используем стандартные имена файлов


def main():
    image_one, image_two = find_image_files()

    print(f"First face: ", image_one)
    print(f"Second face: ", image_two)

    print('\n'+"~" * 10 + " Start recognition " + "~" * 10)
    print(f'- Face Recognition: \t', check_face_recognition(image_one, image_two))
    print(f'- DeepFace: \t\t\t', check_deepface(image_one, image_two))

    print("~" * 15 + " Finished " + "~" * 15)
    x = input('\nType "again" to check one more time.\n'
              'Press "Enter" to exit:\n>> ').lower()
    if x == 'again':
        main()
    else:
        pass


if __name__ == "__main__":
    main()
