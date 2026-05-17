# -------------------------------------------------------------------------
#   INFO
# -------------------------------------------------------------------------
# Name:         Find The Area
# Purpose:      Uses simple formulas in order to find the area of a shape
# Programmer:   Kektsune
# Date:         01/14/2026
# -------------------------------------------------------------------------

#Imports modules
from tkinter import *
import os

#Sets path and finds image locations
base_path = os.path.dirname(os.path.abspath(__file__))

rectangle_image_path = os.path.join(base_path, "Rectangle.png")
right_triangle_image_path = os.path.join(base_path, "Right Triangle.png")
isosceles_triangle_image_path = os.path.join(base_path, "Isosceles Triangle.png")
full_circle_image_path = os.path.join(base_path, "Full Circle.png")
semi_circle_image_path = os.path.join(base_path, "Semi Circle.png")
square_image_path = os.path.join(base_path, "Square.png")

window = Tk()

#Truncates for a cleaner display
def format_number(n):
    if n == int(n):
        return str(int(n))
    else:
        return str(n)


# ----------------------- RECTANGLE ---------------------- #

def backRectangle():
    rectangleDirectionLabel.grid_forget()
    frameRectangle.grid_forget()
    mainMenu()

def submitRectangle():
    try:
        lengthRectangleAnswer = float(lengthRectangleEntry.get())
        widthRectangleAnswer = float(widthRectangleEntry.get())

        fullRectangleAnswer = lengthRectangleAnswer * widthRectangleAnswer

        lengthRectangleString = format_number(lengthRectangleAnswer)
        widthRectangleString = format_number(widthRectangleAnswer)
        fullRectangleString = format_number(fullRectangleAnswer)

        answerRectangleLabel.config(text=lengthRectangleString + " * " + widthRectangleString + " = " + fullRectangleString)
    except ValueError:
        errorLabel = Label(frameRectangle, text="Please enter a valid number!", fg="red")
        errorLabel.pack()

def rectangleMenu():
    global lengthRectangleEntry, widthRectangleEntry, frameRectangle, answerRectangleLabel, rectangleDirectionLabel, rectanglePhotoImage

    title.grid_forget()
    frameMain.grid_forget()
    mainDirections.grid_forget()
    tag.grid_forget()

    rectangleDirectionLabel = Label(window, text='Please enter the following information: ')
    rectangleDirectionLabel.grid(row=0, column=0, columnspan=2)
    
    frameRectangle = Frame(window)
    frameRectangle.grid(row=1, column=0)

    lengthRectangleLabel = Label(frameRectangle, text='Please enter the number of the length below: ')
    lengthRectangleLabel.pack()

    lengthRectangleEntry = Entry(frameRectangle)
    lengthRectangleEntry.pack()

    widthRectangleLabel = Label(frameRectangle, text='Please enter the number of the width below: ')
    widthRectangleLabel.pack()

    widthRectangleEntry = Entry(frameRectangle)
    widthRectangleEntry.pack()

    Label(frameRectangle, text='').pack()

    rectanglePhotoImage = PhotoImage(file=rectangle_image_path)
    photoHolderRectangle = Label(frameRectangle, image=rectanglePhotoImage)
    photoHolderRectangle.pack()

    Label(frameRectangle, text='').pack()

    submitRectangleButton = Button(frameRectangle, text='Submit', command=submitRectangle)
    submitRectangleButton.pack()

    resultsRectangleLabel = Label(frameRectangle, text='Results:')
    resultsRectangleLabel.pack()

    answerRectangleLabel = Label(frameRectangle, text='L * W = A')
    answerRectangleLabel.pack()

    backRectangleButton = Button(frameRectangle, text='Back', command=backRectangle)
    backRectangleButton.pack()

# ----------------------- TRIANGLE ---------------------- #
def triangleMenu():
    global triangleChoiceLabel, triangleChoiceFrame

    title.grid_forget()
    frameMain.grid_forget()
    mainDirections.grid_forget()
    tag.grid_forget()

    triangleChoiceLabel = Label(window, text='Which type of triangle are you working on?: ')
    triangleChoiceLabel.grid(row=0, column=0, columnspan=2)

    triangleChoiceFrame = Frame(window)
    triangleChoiceFrame.grid(row=1, column=0)

    rightAngleTriangle_single = Button(triangleChoiceFrame, text='Right triangle', command=rightAngleSingle)
    rightAngleTriangle_single.grid(row=1, column=0, padx=10, pady=10)

    isoscelesTriangle = Button(triangleChoiceFrame, text='Isosceles triangle', command=isosceles)
    isoscelesTriangle.grid(row=1, column=1, padx=10, pady=10)

    backTriangleButton_1 = Button(triangleChoiceFrame, text='Back', command=backTriangle)
    backTriangleButton_1.grid(row=2, column=0, columnspan=2)

def isosceles():
    global baseTriangleIsoEntry_1, baseTriangleIsoEntry_2, heightTriangleIsoEntry, additionTriangleIsoLabel, answerTriangleIsoLabel, triangleIsoDirectionLabel, frameTriangleIso, submitTriangleIsoButton, isoscelesTrianglePhotoImage
    triangleChoiceFrame.grid_forget()
    triangleChoiceLabel.grid_forget()

    triangleIsoDirectionLabel = Label(window, text='Please enter the following information: ')
    triangleIsoDirectionLabel.grid(row=0, column=0, columnspan=2)
    
    frameTriangleIso = Frame(window)
    frameTriangleIso.grid(row=1, column=0)

    baseTriangleIsoLabel = Label(frameTriangleIso, text='Please enter the number of the first half of the base below: ')
    baseTriangleIsoLabel.pack()

    baseTriangleIsoEntry_1 = Entry(frameTriangleIso)
    baseTriangleIsoEntry_1.pack()

    baseTriangleIsoLabel = Label(frameTriangleIso, text='Please enter the number of the second half of the base below: ')
    baseTriangleIsoLabel.pack()

    baseTriangleIsoEntry_2 = Entry(frameTriangleIso)
    baseTriangleIsoEntry_2.pack()

    heightTriangleIsoLabel = Label(frameTriangleIso, text='Please enter the number of the height below: ')
    heightTriangleIsoLabel.pack()

    heightTriangleIsoEntry = Entry(frameTriangleIso)
    heightTriangleIsoEntry.pack()

    Label(frameTriangleIso, text='').pack()

    isoscelesTrianglePhotoImage = PhotoImage(file=isosceles_triangle_image_path)
    photoHolderIso = Label(frameTriangleIso, image=isoscelesTrianglePhotoImage)
    photoHolderIso.pack()

    Label(frameTriangleIso, text='').pack()

    submitTriangleIsoButton = Button(frameTriangleIso, text='Submit', command=submitTriangleIso)
    submitTriangleIsoButton.pack()

    resultsTriangleIsoLabel = Label(frameTriangleIso, text='Results:')
    resultsTriangleIsoLabel.pack()

    additionTriangleIsoLabel = Label(frameTriangleIso, text='B(first half) + B(second half) = B')
    additionTriangleIsoLabel.pack()

    answerTriangleIsoLabel = Label(frameTriangleIso, text='A = 1/2 * B * H')
    answerTriangleIsoLabel.pack()

    backTriangleIsoButton = Button(frameTriangleIso, text='Back', command=backIsoTriangle)
    backTriangleIsoButton.pack()

def rightAngleSingle():
    global baseTriangleEntry, heightTriangleEntry, answerTriangleLabel, triangleDirectionLabel, frameTriangle, backTriangleButton, answerTriangleIsoLabel, additionTriangleIsoLabel, submitTriangleButton, rightTrianglePhotoImage

    triangleChoiceFrame.grid_forget()
    triangleChoiceLabel.grid_forget()

    triangleDirectionLabel = Label(window, text='Please enter the following information: ')
    triangleDirectionLabel.grid(row=0, column=0, columnspan=2)
    
    frameTriangle = Frame(window)
    frameTriangle.grid(row=1, column=0)

    baseTriangleLabel = Label(frameTriangle, text='Please enter the number of the base below: ')
    baseTriangleLabel.pack()

    baseTriangleEntry = Entry(frameTriangle)
    baseTriangleEntry.pack()

    heightTriangleLabel = Label(frameTriangle, text='Please enter the number of the height below: ')
    heightTriangleLabel.pack()

    heightTriangleEntry = Entry(frameTriangle)
    heightTriangleEntry.pack()

    Label(frameTriangle, text='').pack()

    rightTrianglePhotoImage = PhotoImage(file=right_triangle_image_path)
    photoHolderRightTriangle = Label(frameTriangle, image=rightTrianglePhotoImage)
    photoHolderRightTriangle.pack()

    Label(frameTriangle, text='').pack()

    submitTriangleButton = Button(frameTriangle, text='Submit', command=submitTriangle)
    submitTriangleButton.pack()

    resultsTriangleLabel = Label(frameTriangle, text='Results:')
    resultsTriangleLabel.pack()

    answerTriangleLabel = Label(frameTriangle, text='A = 1/2 * B * H')
    answerTriangleLabel.pack()

    backTriangleButton = Button(frameTriangle, text='Back', command=backRightTriangle)
    backTriangleButton.pack()

def submitTriangle():
    try:
        baseTriangleAnswer = float(baseTriangleEntry.get())
        heightTriangleAnswer = float(heightTriangleEntry.get())

        fullTriangleAnswer = 1 / 2 * baseTriangleAnswer * heightTriangleAnswer

        baseTriangleString = format_number(baseTriangleAnswer)
        heightTriangleString = format_number(heightTriangleAnswer)
        fullTriangleString = format_number(fullTriangleAnswer)

        answerTriangleLabel.config(text="1 / 2 * " + baseTriangleString + " * " + heightTriangleString + " = " + fullTriangleString)
    except ValueError:
        errorLabel = Label(frameTriangle, text="Please enter a valid number!", fg="red")
        errorLabel.pack()

def submitTriangleIso():
    try:
        baseTriangleIsoAnswer_1 = float(baseTriangleIsoEntry_1.get())
        baseTriangleIsoAnswer_2 = float(baseTriangleIsoEntry_2.get())
        heightTriangleIsoAnswer = float(heightTriangleIsoEntry.get())

        baseTriangleIso = baseTriangleIsoAnswer_1 + baseTriangleIsoAnswer_2

        fullTriangleIsoAnswer = 1 / 2 * baseTriangleIso * heightTriangleIsoAnswer

        baseTriangleIsoString_1 = format_number(baseTriangleIsoAnswer_1)
        baseTriangleIsoString_2 = format_number(baseTriangleIsoAnswer_2)
        baseTriangleIsoString = format_number(baseTriangleIso)
        heightTriangleIsoString = format_number(heightTriangleIsoAnswer)
        fullTriangleIsoString = format_number(fullTriangleIsoAnswer)

        additionTriangleIsoLabel.config(text=baseTriangleIsoString_1 + " + " + baseTriangleIsoString_2 + " = " + baseTriangleIsoString)
        answerTriangleIsoLabel.config(text="1 / 2 * " + baseTriangleIsoString + " * " + heightTriangleIsoString + " = " + fullTriangleIsoString)
    except ValueError:
        errorLabel = Label(frameTriangleIso, text="Please enter a valid number!", fg="red")
        errorLabel.pack()

def backTriangle():
    triangleChoiceFrame.grid_forget()
    triangleChoiceLabel.grid_forget()
    mainMenu()

def backRightTriangle():
    triangleDirectionLabel.grid_forget()
    frameTriangle.grid_forget()
    backTriangleButton.grid_forget()
    answerTriangleLabel.grid_forget()
    triangleMenu()

def backIsoTriangle():
    triangleIsoDirectionLabel.grid_forget()
    frameTriangleIso.grid_forget()
    submitTriangleIsoButton.grid_forget()
    additionTriangleIsoLabel.grid_forget()
    answerTriangleIsoLabel.grid_forget()
    triangleMenu()

# ----------------------- SQUARE ---------------------- #
def squareMenu():
    global squareDirectionLabel, frameSquare, sideSquareEntry, answerSquareLabel, squarePhotoImage

    title.grid_forget()
    frameMain.grid_forget()
    mainDirections.grid_forget()
    tag.grid_forget()

    squareDirectionLabel = Label(window, text='Please enter the following information: ')
    squareDirectionLabel.grid(row=0, column=0, columnspan=2)
    
    frameSquare = Frame(window)
    frameSquare.grid(row=1, column=0)

    sideSquareLabel = Label(frameSquare, text='Please enter a side: ')
    sideSquareLabel.pack()

    sideSquareEntry = Entry(frameSquare)
    sideSquareEntry.pack()

    Label(frameSquare, text='').pack()

    squarePhotoImage = PhotoImage(file=square_image_path)
    photoHolderSquare = Label(frameSquare, image=squarePhotoImage)
    photoHolderSquare.pack()

    Label(frameSquare, text='').pack()

    submitSquareButton = Button(frameSquare, text='Submit', command=submitSquare)
    submitSquareButton.pack()

    resultsSquareLabel = Label(frameSquare, text='Results:')
    resultsSquareLabel.pack()

    answerSquareLabel = Label(frameSquare, text='A = s^2')
    answerSquareLabel.pack()

    backSquareButton = Button(frameSquare, text='Back', command=backSquare)
    backSquareButton.pack()

def backSquare():
    squareDirectionLabel.grid_forget()
    frameSquare.grid_forget()
    mainMenu()

def submitSquare():
    try:
        sideSquareAnswer = float(sideSquareEntry.get())

        fullSquareAnswer = sideSquareAnswer * sideSquareAnswer

        sideSquareString = format_number(sideSquareAnswer)
        fullSquareString = format_number(fullSquareAnswer)

        answerSquareLabel.config(text=fullSquareString + " = " + sideSquareString +"^2")

        answerSquareLabel.config(text=fullSquareString + " = " + sideSquareString +"^2")
    except ValueError:
        errorLabel = Label(frameSquare, text="Please enter a valid number!", fg="red")
        errorLabel.pack()
# ----------------------- CIRCLE ---------------------- #
def circleMenu():
    global circleChoiceLabel, circleChoiceFrame

    title.grid_forget()
    frameMain.grid_forget()
    mainDirections.grid_forget()
    tag.grid_forget()

    circleChoiceLabel = Label(window, text='Which type of circle are you working on?: ')
    circleChoiceLabel.grid(row=0, column=0, columnspan=2)

    circleChoiceFrame = Frame(window)
    circleChoiceFrame.grid(row=1, column=0)

    circle = Button(circleChoiceFrame, text='Full circle', command=fullCircle)
    circle.grid(row=2, column=0, padx=10, pady=10)

    semiCircleButton = Button(circleChoiceFrame, text='semi-Circle', command=semiCircle)
    semiCircleButton.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    backCircleButton = Button(circleChoiceFrame, text='Back', command=backCircle)
    backCircleButton.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

def backCircle():
    circleChoiceLabel.grid_forget()
    circleChoiceFrame.grid_forget()
    mainMenu()

def semiCircle():
    global semiDirectionLabel, frameSemi, radiusSemiEntry, answerSemiLabel_1, answerSemiLabel_2, semiCirclePhotoImage

    circleChoiceLabel.grid_forget()
    circleChoiceFrame.grid_forget()

    semiDirectionLabel = Label(window, text='Please enter the following information: ')
    semiDirectionLabel.grid(row=0, column=0, columnspan=2)

    frameSemi = Frame(window)
    frameSemi.grid(row=1, column=0)

    radiusSemiLabel = Label(frameSemi, text='Please enter the radius: ')
    radiusSemiLabel.pack()

    radiusSemiEntry = Entry(frameSemi)
    radiusSemiEntry.pack()

    Label(frameSemi, text='').pack()

    semiCirclePhotoImage = PhotoImage(file=semi_circle_image_path)
    photoHolderSemiCircle = Label(frameSemi, image=semiCirclePhotoImage)
    photoHolderSemiCircle.pack()

    Label(frameSemi, text='').pack()

    submitSemiButton = Button(frameSemi, text='Submit', command=semiSubmit)
    submitSemiButton.pack()

    resultsSemiLabel = Label(frameSemi, text='Results: ')
    resultsSemiLabel.pack()

    answerSemiLabel_1 = Label(frameSemi, text='Version 1: A = 1/2 * π * R^2')
    answerSemiLabel_1.pack()

    answerSemiLabel_2 = Label(frameSemi, text='Version 2: Aπ = 1/2 * π * R^2')
    answerSemiLabel_2.pack()

    backSemiButton = Button(frameSemi, text='Back', command=backSemi)
    backSemiButton.pack()

def semiSubmit():
    try:
        radiusSemiAnswer = float(radiusSemiEntry.get())

        semiAreaAnswerOne = 1/2 * 3.14 * radiusSemiAnswer * radiusSemiAnswer
        semiAreaAnswerTwo = 1/2 * radiusSemiAnswer * radiusSemiAnswer

        radiusSemiAnswerString = format_number(radiusSemiAnswer)
        semiAreaAnswerStringOne = format_number(semiAreaAnswerOne)
        semiAreaAnswerStringTwo = format_number(semiAreaAnswerTwo)

        answerSemiLabel_1.config(text="Version 1: " + semiAreaAnswerStringOne + " = 1 / 2 * π * " + radiusSemiAnswerString + "^2")
        answerSemiLabel_2.config(text="Version 2: " + semiAreaAnswerStringTwo + "π = 1 / 2 * π * " + radiusSemiAnswerString + "^2")
    except ValueError:
        errorLabel = Label(frameSemi, text="Please enter a valid number!", fg="red")
        errorLabel.pack()

def backSemi():
    semiDirectionLabel.grid_forget()
    frameSemi.grid_forget()
    circleMenu()

def fullCircle():
    global diaCircleEntry, radiusCircleLabel, answerCircleLabel, answerCircleLabel_2, circleDirectionLabel, frameCircle, fullCirclePhotoImage

    circleChoiceLabel.grid_forget()
    circleChoiceFrame.grid_forget()

    circleDirectionLabel = Label(window, text='Please enter the following information: ')
    circleDirectionLabel.grid(row=0, column=0, columnspan=2)
    
    frameCircle = Frame(window)
    frameCircle.grid(row=1, column=0)

    diaCircleLabel = Label(frameCircle, text='Please enter the diameter: ')
    diaCircleLabel.pack()

    diaCircleEntry = Entry(frameCircle)
    diaCircleEntry.pack()

    Label(frameCircle, text='').pack()

    fullCirclePhotoImage = PhotoImage(file=full_circle_image_path)
    photoHolderFullCircle = Label(frameCircle, image=fullCirclePhotoImage)
    photoHolderFullCircle.pack()

    Label(frameCircle, text='').pack()

    submitCircleButton = Button(frameCircle, text='Submit', command=submitFullCircle)
    submitCircleButton.pack()

    resultsCircleLabel = Label(frameCircle, text='Results: ')
    resultsCircleLabel.pack()

    radiusCircleLabel = Label(frameCircle, text='R = 1/2 * d')
    radiusCircleLabel.pack()

    answerCircleLabel = Label(frameCircle, text='Version 1: A = π * R ^ 2')
    answerCircleLabel.pack()

    answerCircleLabel_2 = Label(frameCircle, text='Version 2: Aπ = π * R ^ 2')
    answerCircleLabel_2.pack()

    backCircleButton = Button(frameCircle, text='Back', command=backFullCircle)
    backCircleButton.pack()

def submitFullCircle():
    try:
        diaFullCircleAnswer = float(diaCircleEntry.get())

        radiusFullCircleAnswer = 1/2 * diaFullCircleAnswer

        areaFullCircleAnswer_1 = 3.14 * radiusFullCircleAnswer * radiusFullCircleAnswer
        areaFullCircleAnswer_2 = radiusFullCircleAnswer * radiusFullCircleAnswer

        diaFullCircleString = format_number(diaFullCircleAnswer)
        radiusFullCircleString = format_number(radiusFullCircleAnswer)
        areaFullCircleString_1 = format_number(areaFullCircleAnswer_1)
        areaFullCircleString_2 = format_number(areaFullCircleAnswer_2)

        radiusCircleLabel.config(text=radiusFullCircleString + " = 1 / 2 * " + diaFullCircleString)
        answerCircleLabel.config(text="Version 1: " + areaFullCircleString_1 + " = π * " + radiusFullCircleString + "^2")
        answerCircleLabel_2.config(text="Version 2: " + areaFullCircleString_2 + "π = π * " + radiusFullCircleString + "^2")
    except ValueError:
        errorLabel = Label(frameCircle, text="Please enter a valid number!", fg="red")
        errorLabel.pack()

def backFullCircle():
    circleDirectionLabel.grid_forget()
    frameCircle.grid_forget()
    circleMenu()

# ----------------------- MAIN ---------------------- #
def mainMenu():
    global title, frameMain, mainDirections, tag

    window.title("Find The Area")

    title = Label(window, text="Welcome to Find The Area!")
    title.grid(row=0, column=0, columnspan=2)

    mainDirections = Label(window, text='Click one of the buttons below to find the area of the shape!')
    mainDirections.grid(row=1, column=0, columnspan=2)

    frameMain = Frame(window)
    frameMain.grid(row=2, column=0, columnspan=2)

    rectangle = Button(frameMain, text='Rectangle', command=rectangleMenu)
    rectangle.grid(row=2, column=0, padx=10, pady=10)

    triangle = Button(frameMain, text='Triangle', command=triangleMenu)
    triangle.grid(row=2, column=1, padx=10, pady=10)

    square = Button(frameMain, text='Square', command=squareMenu)
    square.grid(row=2, column=2, padx=10, pady=10)

    circle = Button(frameMain, text='Circle', command=circleMenu)
    circle.grid(row=3, column=0, padx=10, pady=10)

    tag = Label(window, text="By: Kektsune")
    tag.grid(row=4, column=0, columnspan=2)

mainMenu()

window.mainloop()