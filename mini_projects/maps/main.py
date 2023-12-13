import customtkinter as ctk
from settings import *
import tkintermapview
from geopy.geocoders import Nominatim

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		ctk.set_appearance_mode('light')
		self.geometry('1200x800+100+50')
		self.minsize(800,600)
		self.title('Map')
		self.iconbitmap('map.ico')

		# data 
		self.input_string = ctk.StringVar()

		# layout 
		self.rowconfigure(0, weight = 1, uniform = 'a')
		self.columnconfigure(0, weight = 2, uniform = 'a')
		self.columnconfigure(1, weight = 8, uniform = 'a')

		# widgets 
		self.map_widgt = MapWidget(self, self.input_string, self.submit_location)

		self.mainloop()

	def submit_location(self, event):
		# get data
		geolocator = Nominatim(user_agent = 'my-user')
		location = geolocator.geocode(self.input_string.get())

		# update map
		if location:
			self.map_widgt.set_address(location.address)

			# clear the input
			self.input_string.set('')
		else:
			print('invalid')

class MapWidget(tkintermapview.TkinterMapView):
	def __init__(self, parent, input_string, submit_location):
		super().__init__(master = parent)
		self.grid(row = 0, column = 1, sticky = 'nsew')

		# entry 
		LocationEntry(self, input_string, submit_location)

		# self.set_tile_server(TERRAIN_URL)

class LocationEntry(ctk.CTkEntry):
	def __init__(self, parent, input_string, submit_location):
		super().__init__(
			master = parent, 
			textvariable = input_string,
			corner_radius = 0,
			border_width = 4,
			fg_color = ENTRY_BG,
			border_color = ENTRY_BG,
			text_color = TEXT_COLOR,
			font = ctk.CTkFont(family = TEXT_FONT, size = TEXT_SIZE))
		self.place(relx = 0.5, rely = 0.95, anchor = 'center')

		self.bind('<Return>', submit_location)

		# exercise:
		# if the input is invalid print 'invalid'

App()