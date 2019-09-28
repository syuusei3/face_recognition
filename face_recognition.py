import face_recognition
import cv2
import numpy as np
#動画を指定
video_capture = cv2.VideoCapture("yui.mp4")

# 人物指定　追加で人を増やせる
known_image = face_recognition.load_image_file("yui.jpg")
biden_encoding = face_recognition.face_encodings(known_image)[0]

# ２つめの人物指定
unknown_image = face_recognition.load_image_file("ken.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#エンコーディングした顔と名前の配列を作成
known_face_encodings = [
    biden_encoding,
    unknown_encoding
]
known_face_names = [
    "Yui Aragaki",
    "Ken Watababe"
]
# いくつかの変数を初期化
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # ビデオのフレームを読み込む
    ret, frame = video_capture.read()
    # ビデオのフレームを1/4サイズにして、顔認識処理を高速化
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # 画像をBGRカラー(OpenCV)からRGBカラー(face_recognition)に変換
    rgb_small_frame = small_frame[:, :, ::-1]
    #時間を節約するためにフレームのみを処理
    if process_this_frame:
        # 現在のビデオフレーム内のすべでの顔を読み込む
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 顔が既知の顔と一致するか確認する
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            # 顔との距離が最小のものを使用
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    # 結果の表示
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        #フレームを1/4に縮小したため、顔の位置を調整
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 顔のまわりにボックスを表示
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 顔の下に名前のついてラベルの表示
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 結果の表示
    cv2.imshow('Video', frame)

    # 'q'を押して処理の停止
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラへの主導権をもどす
video_capture.release()
cv2.destroyAllWindows()
