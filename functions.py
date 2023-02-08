# def read_qr_code():
#     import cv2
#     cap = cv2.VideoCapture(0)
#     while True:
#         _, frame = cap.read()
#         decoded_data, _, _ = cv2.QRCodeDetector().detectAndDecode(frame)
#         if decoded_data:
#             data = decoded_data
#             cycle_number, farm_name, barn_number = data.split(",")
#             print(data)
#             cycle_number = cycle_number.split(":")[1]
#             farm_name = farm_name.split(":")[1]
#             barn_number = barn_number.split(":")[1]
#             return cycle_number, farm_name, barn_number
#         cv2.imshow("Webcam", frame)
#         key = cv2.waitKey(1)
#         if key == 27:
#             break
#     cap.release()
#     cv2.destroyAllWindows()


def check_session(intended_job_title):
    from flask import session
    if 'username' not in session:
        from flask import redirect
        from flask import url_for
        return redirect(url_for('view_login'))
    from User.UserModel import get_user_id_by_username
    session_user = get_user_id_by_username(session['username'])
    if session_user['jobTitle'] != intended_job_title:
        return "Access Denied"
