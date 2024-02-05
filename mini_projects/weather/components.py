import customtkinter as ctk
import datetime, calendar

class SimplePanel(ctk.CTkFrame):
	def __init__(self, parent, weather, col, row, color):
		super().__init__(master = parent, fg_color = color['main'], corner_radius = 0)
		self.grid(column = col, row = row, sticky = 'nsew')

		# layout 
		self.rowconfigure(0, weight = 1, uniform = 'a')
		self.columnconfigure((0,1), weight = 1, uniform = 'a')

		# widgets 
		temp_frame = ctk.CTkFrame(self, fg_color = 'transparent')
		ctk.CTkLabel(temp_frame, text = f"{weather['temp']}\N{DEGREE SIGN}", font = ctk.CTkFont(family = 'Calibri', size = 50), text_color = color['text']).pack()
		ctk.CTkLabel(temp_frame, text = f"feels like: {weather['feels_like']}\N{DEGREE SIGN}", font = ctk.CTkFont(family = 'Calibri', size = 16), text_color = color['text']).pack()
		temp_frame.grid(row = 0, column = 0)

class DatePanel(ctk.CTkFrame):
	def __init__(self, parent, location, col, row, color):
		super().__init__(master = parent, fg_color = color['main'], corner_radius = 0)
		self.grid(column = col, row = row, sticky = 'nsew')

		# location 
		location_frame = ctk.CTkFrame(self, fg_color = 'transparent')
		ctk.CTkLabel(
			location_frame, 
			text = f"{location['city']}, ", 
			font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'),
			text_color = color['text']).pack(side = 'left')
		ctk.CTkLabel(location_frame, 
			text = f"{location['country']}",
			font = ctk.CTkFont(family = 'Calibri', size = 20),
			text_color = color['text']).pack(side = 'left')
		location_frame.pack(side = 'left', padx = 10)

		# date 
		day, weekday, suffix, month = get_time_info()
		ctk.CTkLabel(self, 
			text = f"{weekday[:3]}, {day}{suffix} {calendar.month_name[month]}",
			font = ctk.CTkFont(family = 'Calibri', size = 20),
			text_color = color['text']).pack(side = 'right', padx = 10)

class HorizontalForecastPanel(ctk.CTkFrame):
	def __init__(self, parent, forecast_data, col, row, rowspan, divider_color):
		super().__init__(master = parent, fg_color = '#FFF')
		self.grid(column = col, row = row, rowspan = rowspan, sticky = 'nsew', padx = 6, pady = 6)

		# widgets 
		for index, info in enumerate(forecast_data.items()):
			frame = ctk.CTkFrame(self, fg_color = 'transparent')
			
			# data
			year, month, day = info[0].split('-')
			weekday = list(calendar.day_name)[datetime.date(int(year), int(month), int(day)).weekday()][:3]
			
			# layout
			frame.columnconfigure(0, weight = 1, uniform = 'a')
			frame.rowconfigure(0, weight = 5, uniform = 'a')
			frame.rowconfigure(1, weight = 2, uniform = 'a')
			frame.rowconfigure(2, weight = 1, uniform = 'a')

			# widgets 
			ctk.CTkLabel(frame, text = f"{info[1]['temp']}\N{DEGREE SIGN}", text_color = '#444', font = ('Calibri', 22)).grid(row = 1, column = 0, sticky = 'n')
			ctk.CTkLabel(frame, text = weekday, text_color = '#444').grid(row = 2, column = 0)
			frame.pack(side = 'left', expand = True, fill = 'both', padx = 5, pady = 5)

			# exercise:
			# add divider lines with the divider color 
			# do not add a divider after the final frame
			if index < len(forecast_data) - 1:
				ctk.CTkFrame(self, fg_color = divider_color, width = 2).pack(side = 'left', fill = 'both')


def get_time_info():
	month = datetime.datetime.today().month
	day = datetime.datetime.today().day
	weekday = list(calendar.day_name)[datetime.datetime.today().weekday()]

	match day % 10:
		case 1: suffix = 'st'
		case 2: suffix = 'nd'
		case 3: suffix = 'rd'
		case _: suffix = 'th'

	return day, weekday, suffix, month