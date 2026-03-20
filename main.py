import cv2

# Load face and eye detectors
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status = "No Face"
    direction = "No Face"
    score = 0
    final_status = "No Face"

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        score = 100

        center_x = x + w // 2
        frame_center = frame.shape[1] // 2

        if center_x < frame_center - 50:
            direction = "Looking Left"
        elif center_x > frame_center + 50:
            direction = "Looking Right"
        else:
            direction = "Looking Center"

        if direction != "Looking Center":
            score -= 20

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Count eyes
        if len(eyes) == 0:
            status = "Drowsy"
        else:
            status = "Active"

        if status == "Drowsy":
            score -= 30

        if score > 70:
            final_status = "Attentive"
        elif score > 40:
            final_status = "Distracted"
        else:
            final_status = "Drowsy"

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255,0,0), 2)

        # Show status
    cv2.putText(frame, status, (50,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.putText(frame, direction, (50,100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        
    cv2.putText(frame, f"Score: {score}", (50,150),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, final_status, (50,200),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    cv2.imshow("Attention Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()