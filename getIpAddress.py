import tkinter
import pygeoip

class FindLocation (object):
    def __init__(self):
        self.gi   = pygeoip.GeoIP("./GeoLiteCity.dat")
        self.root = tkinter.Tk()
        self.root.title("get address")
        self.ip_input      = tkinter.Entry(self.root, width = 100)
        self.display_info  = tkinter.Listbox(self.root, width = 100)
        self.result_button = tkinter.Button(self.root, command = self.find_position, text = "Search~")
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()
    def find_position(self):
        self.ip_addr = self.ip_input.get()
        aim = self.gi.record_by_name(self.ip_addr)
        try:
            city        = aim['city']
            country     = aim['country_name']
            region_code = aim['region_code']
            longitude   = aim['longitude']
            latitude    = aim['latitude']
        except:
            pass
        the_ip_info = ["所在纬度:" + str(latitude), "所在经度:" + str(longitude), "地域代号:" + str(region_code),
                       "所在城市:" + str(city), "所在国家或地区:" + str(country), "需要查询的ip:" + str(self.ip_addr)]
        for item in range(10):
            self.display_info.insert(0, "")
        for item in the_ip_info:
            self.display_info.insert(0, item)
        return the_ip_info
def main():
    FL = FindLocation()
    FL.gui_arrang()
    tkinter.mainloop()
    pass
if __name__ == "__main__":
    main()