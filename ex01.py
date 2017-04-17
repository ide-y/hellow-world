import cv2

def main():
    img = cv2.imread("lena.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Show",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
