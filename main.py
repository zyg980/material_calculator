from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
import math

# 定义材料密度（单位：g/cm³）
material_densities = {
    "铝": 2.7,
    "铜": 8.96,
    "铁": 7.874,
    "金": 19.3,
    "银": 10.49,
    "铅": 11.34
}

class MaterialCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # 创建形状选择器
        self.shape_spinner = Spinner(
            text='选择形状',
            values=('长方体', '圆柱体', '圆管'),
            size_hint=(1, None),
            height='48dp'
        )
        self.shape_spinner.bind(text=self.update_fields)
        self.add_widget(self.shape_spinner)
        
        # 创建输入框网格
        self.input_grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.input_grid.bind(minimum_height=self.input_grid.setter('height'))
        self.add_widget(self.input_grid)
        
        # 创建输入字段
        self.inputs = {}
        self.create_inputs()
        
        # 创建材料选择器
        self.material_spinner = Spinner(
            text='选择材料',
            values=tuple(material_densities.keys()),
            size_hint=(1, None),
            height='48dp'
        )
        self.add_widget(self.material_spinner)
        
        # 创建计算按钮
        self.calculate_button = Button(
            text='计算',
            size_hint=(1, None),
            height='48dp'
        )
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)
        
        # 创建结果标签
        self.result_label = Label(
            text='质量: ',
            size_hint=(1, None),
            height='48dp'
        )
        self.add_widget(self.result_label)
        
        # 添加版权信息
        self.copyright_label = Label(
            text='©版权所有：金峡能源装备有限公司',
            size_hint=(1, None),
            height='48dp'
        )
        self.add_widget(self.copyright_label)
    
    def create_inputs(self):
        self.inputs = {
            'length': TextInput(hint_text='长度 (mm)', multiline=False),
            'width': TextInput(hint_text='宽度 (mm)', multiline=False),
            'height': TextInput(hint_text='高度 (mm)', multiline=False),
            'diameter': TextInput(hint_text='直径 (mm)', multiline=False),
            'outer_diameter': TextInput(hint_text='外径 (mm)', multiline=False),
            'inner_diameter': TextInput(hint_text='内径 (mm)', multiline=False)
        }

    def update_fields(self, instance, value):
        self.input_grid.clear_widgets()
        if value == '长方体':
            self.show_inputs(['length', 'width', 'height'])
        elif value == '圆柱体':
            self.show_inputs(['diameter', 'height'])
        elif value == '圆管':
            self.show_inputs(['outer_diameter', 'inner_diameter', 'height'])
    
    def show_inputs(self, fields):
        for field in fields:
            self.input_grid.add_widget(Label(text=self.inputs[field].hint_text))
            self.input_grid.add_widget(self.inputs[field])
    
    def calculate(self, instance):
        try:
            shape = self.shape_spinner.text
            material = self.material_spinner.text
            
            if shape not in ['长方体', '圆柱体', '圆管']:
                self.result_label.text = '错误: 请选择形状'
                return
                
            if material not in material_densities:
                self.result_label.text = '错误: 请选择材料'
                return
            
            volume = self.calculate_volume(shape)
            if volume is None:
                return
                
            density = material_densities[material]
            mass = volume * density / 1000  # 转换为千克
            
            self.result_label.text = f'质量: {mass:.2f} 千克'
        except ValueError:
            self.result_label.text = '错误: 请输入有效的数值'
        except Exception as e:
            self.result_label.text = f'错误: {str(e)}'
    
    def calculate_volume(self, shape):
        try:
            if shape == '长方体':
                length = float(self.inputs['length'].text)
                width = float(self.inputs['width'].text)
                height = float(self.inputs['height'].text)
                return (length * width * height) / 1000
            elif shape == '圆柱体':
                diameter = float(self.inputs['diameter'].text)
                height = float(self.inputs['height'].text)
                radius = diameter / 2
                return (math.pi * radius**2 * height) / 1000
            elif shape == '圆管':
                outer_diameter = float(self.inputs['outer_diameter'].text)
                inner_diameter = float(self.inputs['inner_diameter'].text)
                height = float(self.inputs['height'].text)
                if inner_diameter >= outer_diameter:
                    self.result_label.text = '错误: 内径不能大于或等于外径'
                    return None
                outer_radius = outer_diameter / 2
                inner_radius = inner_diameter / 2
                return (math.pi * (outer_radius**2 - inner_radius**2) * height) / 1000
        except ValueError:
            self.result_label.text = '错误: 请输入有效的数值'
            return None

class MaterialCalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # 设置背景色
        return MaterialCalculator()

if __name__ == '__main__':
    MaterialCalculatorApp().run()