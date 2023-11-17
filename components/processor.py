import cv2
import numpy as np
import pandas as pd
from components.video import Video


class Processor:

    def __init__(self, fp, scale, md, p1, p2, min_r, max_r):
        self.vid = Video(fp, 12)
        self.frames = self.vid.get_frames()
        self.scale = scale
        self.md = md
        self.p1 = p1
        self.p2 = p2
        self.min_r = min_r
        self.max_r = max_r

    def run(self):
        count = 0
        res = []
        circle_pos = list()
        num_circles = 2
        for frame in self.frames:
            count += 1
            print("processing frame", count * self.vid.get_capture_count())
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            blurred = cv2.GaussianBlur(frame, (5, 5), 0)
            gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
            edges = cv2.Sobel(gray, cv2.CV_8UC1, 1, 0, ksize=3)
            # cv2.imshow("Detected Circle", edges)
            # cv2.waitKey(0)
            detected_circles = cv2.HoughCircles(edges,
                                                cv2.HOUGH_GRADIENT, self.md, self.p1, self.p2,
                                                self.min_r, minRadius=self.max_r)

            # Draw circles that are detected.
            if detected_circles is not None:

                # Convert the circle parameters a, b and r to integers.
                detected_circles = np.uint16(np.around(detected_circles))

                seconds = (count * self.vid.get_capture_count()) // 25
                if seconds % 60 < 10:
                    time = f"{seconds // 60}:0{seconds % 60}"
                else:
                    time = f"{seconds // 60}:{seconds % 60}"
                data = [time]
                for i in range(num_circles):
                    data.append("--")
                    data.append("--")

                for pt in detected_circles[0, :]:
                    if isinstance(pt, np.ndarray):
                        a, b, r = pt[0], pt[1], pt[2]
                        print(a, b)

                        if len(circle_pos) == 0:
                            circle_pos.append(a)
                            circle_ID = 1
                        else:
                            existing = False
                            cir_count = 1
                            for circle in circle_pos:
                                if (circle - 300) <= a <= (circle + 300):
                                    circle_ID = cir_count
                                    existing = True
                                cir_count += 1

                            if not existing:
                                if len(circle_pos) == num_circles:
                                    break
                                circle_pos.append(a)
                                circle_ID = cir_count

                        # # Draw the circumference of the circle.
                        # cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
                        #
                        # # Draw a small circle (of radius 1) to show the center.
                        # cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
                        #
                        # cv2.imshow("Detected Circle", frame)
                        # cv2.waitKey(0)

                        circumference = (2 * np.pi * r) / 4.54
                        idx = 1 + (2 * (circle_ID - 1))
                        print(circle_pos, idx)
                        data[idx] = "Circle " + str(circle_ID)
                        data[idx+1] = circumference

                        print(circumference, "micrometers")

                res.append(data)

            else:
                res.append(["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"])
                print("no circles")

        columns = ["Time"]
        for i in range(num_circles):
            columns.append("Circle")
            columns.append("Circumference")
        df = pd.DataFrame(res, columns=columns)
        df.to_excel("../output.xlsx", index=False)

# img = cv2.imread('../resources/example.PNG', cv2.IMREAD_COLOR)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # gray_blurred = cv2.blur(gray, (14, 14), cv2.BORDER_DEFAULT)
#
# detected_circles = cv2.HoughCircles(gray,
#                                     cv2.HOUGH_GRADIENT, 1, 15, 180,
#                                     30)
#
# # canny = cv2.Canny(gray, threshold1=100, threshold2=300)
# # cv2.imshow('Edges', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# # Draw circles that are detected.
# if detected_circles is not None:
#
#     # Convert the circle parameters a, b and r to integers.
#     detected_circles = np.uint16(np.around(detected_circles))
#
#     for pt in detected_circles[0, :]:
#         a, b, r = pt[0], pt[1], pt[2]
#
#         circumference = (2 * np.pi * r) / 4.54
#         print(circumference, "micrometers")
#         # Draw the circumference of the circle.
#         cv2.circle(img, (a, b), r, (0, 255, 0), 2)
#
#         # Draw a small circle (of radius 1) to show the center.
#         cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
#
#     cv2.imshow("Detected Circle", img)
#     cv2.waitKey(0)
#
# else:
#     print("no circles")
