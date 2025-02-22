from epd4in2b_driver import EPD_4in2_B
from writer import Writer
import freesans20 as font

content = "A whisper of snow, a frigid kiss,\nNorthwest winds in chilling bliss.\nSun obscured, a cloudy hold,\nFourteen Fahrenheit, a winter's scold.\n"

def updateScren(text):
    epd = EPD_4in2_B()

    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)

    wri = Writer(epd.imageblack, font, True)
    Writer.set_textpos(epd.imageblack, 10, 0)  # verbose = False to suppress console output
    wri.printstring(text, True)

    wri2 = Writer(epd.imagered, font, True)
    Writer.set_textpos(epd.imagered, 100, 0)  # verbose = False to suppress console output
    wri2.printstring(text, True)

    epd.EPD_4IN2B_Display(epd.buffer_black, epd.buffer_red)
    epd.Sleep()

updateScren(content)
