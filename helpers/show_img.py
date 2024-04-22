from tkinter import Tk


root = Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()


def img_helper_dimension(img, width=None, height=None):
    img_height, img_width = img.shape[:2]

    if height is None and width is None:
        if img_height > screen_h or img_width > screen_w:
            rapporto_h = screen_h / img_height
            rapporto_w = screen_w / img_width
            rapporto = min(rapporto_h, rapporto_w)
            img_height = int(img_height * rapporto) - 90
            img_width = int(img_width * rapporto)

    if height is not None:
        img_height = height

    if width is not None:
        img_width = width

    return img_width, img_height


def resize(cv2, img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)


def show_resized_img(cv2, img, width=None, height=None):
    img_width, img_height = img_helper_dimension(img, width, height)

    resized_image = resize(cv2, img, img_width, img_height)

    cv2.namedWindow("Img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Img", img_width, img_height)
    cv2.imshow("Img", resized_image)

    x = (int(screen_w/2) - int(img_width/2))
    cv2.moveWindow("Img", x, 0)

    return img


def show_img(cv2, img):

    _, img_width = img.shape[:2]

    cv2.namedWindow("Img", cv2.WINDOW_NORMAL)
    cv2.imshow("Img", img)

    x = (int(screen_w/2) - int(img_width/2))
    cv2.moveWindow("Img", x, 0)

    return img
