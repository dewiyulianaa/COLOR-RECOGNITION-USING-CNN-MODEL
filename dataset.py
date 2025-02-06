import cv2
import os

# Fungsi untuk membuat folder penyimpanan gambar
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Fungsi untuk merekam dan menyimpan dataset secara real-time
def capture_dataset_realtime(gesture_name, output_directory, cam_index=0, num_samples=100):
    create_directory(output_directory)

    cap = cv2.VideoCapture(cam_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print(f"Merekam dataset untuk gestur: {gesture_name}")

    num_captures = 1
    while num_captures < num_samples:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)  # Flip video horizontally (optional)

        # Menambahkan bingkai di sekitar area tampilan
        border_color = (0, 255, 0)  # Warna bingkai (contoh: hijau)
        border_thickness = 10  # Ketebalan bingkai
        frame = cv2.copyMakeBorder(frame, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

        # Mengubah ukuran gambar masukan menjadi (150, 150)
        frame = cv2.resize(frame, (150, 150))

        cv2.putText(frame, f"Capture: {num_captures + 1}/{num_samples}", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
        cv2.imshow("Capturing Dataset", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Press 'Esc' to exit
            break
        elif key == ord("c"):  # Press 'c' to capture the frame
            image_name = os.path.join(output_directory, f"{gesture_name}_{num_captures + 1}.jpg")
            cv2.imwrite(image_name, frame)
            print(f"Gambar {num_captures + 1} tersimpan: {image_name}")
            num_captures += 1

    cap.release()
    cv2.destroyAllWindows()

# Contoh penggunaan fungsi untuk merekam dataset gestur "tangan terbuka" secara real-time
capture_dataset_realtime("biru", "dataset/biru", cam_index=0, num_samples=50)
