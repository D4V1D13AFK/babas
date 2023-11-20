import flet as ft
import serial
import time

puerto_arduino = 'COM6'

arduino = serial.Serial(puerto_arduino, 9600)
time.sleep(2)

class Bottom(ft.UserControl):
    def __init__(self, name: str, letter: str, color, time = 0.05):
        super().__init__()
        self.name = name
        self.color = color
        self.time = time
        self.letter = letter
        self.run = False
        
    def build(self):
        return ft.GestureDetector(
        on_tap_down=self.click,
        on_tap_up=self.stop,
        content= ft.Container(
                    content=ft.Text(self.name),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=self.color,
                    border_radius=10,
                ),
        )
                
    def loop(self):
        while True:
          print(self.letter)
          arduino.write(self.letter.encode("utf-8"))
          time.sleep(self.time)
          if self.run == False:
            break
                
    def stop(self, e):
        self.run= False
          
    def click(self, e):
        self.run = True
        self.loop()
    
def main(page: ft.Page):
    page.title = "OBRA DEL ALBAÑIL DEL SOFTWARE Y EL CHALAN QUE SE VA A MORIR EN EL COLADO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    right_wrist = Bottom('right_wrist',"J", ft.colors.CYAN)
    
    left_wrist = Bottom('left_wrist',"K", ft.colors.LIGHT_BLUE_700)
    
    left_shoulder = Bottom('left_shoulder', "L", ft.colors.GREEN)
    
    right_shoulder = Bottom('right_shoulder',"R", ft.colors.RED)
    
    right_elbow = Bottom('right_elbow',"E", ft.colors.PURPLE)
    
    left_elbow = Bottom('left_elbow',"H", ft.colors.BLUE)
    
    Open_gripper = Bottom('Open_gripper',"D", ft.colors.BLACK)
    
    close_gripper = Bottom('Close_gripper',"A", ft.colors.PINK)
    
   
    
    list_bottoms = [left_shoulder, right_shoulder,
                    right_elbow,left_elbow,
                    right_wrist,left_wrist,
                    Open_gripper,close_gripper]
    
    bottoms = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(
        ft.Column([
            ft.Container(content=bottoms,alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ))

    for i in list_bottoms:
        bottoms.controls.append(i)

    page.update()

ft.app(target=main)