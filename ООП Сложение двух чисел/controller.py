import model
import view

def button_click():
    value_a = view.get_data()
    value_b = view.get_data()
    value_c = view.get_data()
    model.inits(value_a, value_b, value_c)
    res = model.sum()
    view.print_data(res)