# Raspberry Pi + Arduino Brewery Controller
This project will incorporate some changes from two awesome open source projects: [RasPiBrew](https://github.com/steve71/RasPiBrew) and [BrewPi](http://BrewPi.com)
A lot of this is bound to change.  I will be blogging about this on http://brwry.com/

## Notable projects / Inspiration:
I'd like to thank the following for their awesome projects which served as inspiration for my own:

* [BrewPi](http://brewpi.com/) - [GitHub](https://github.com/BrewPi)
* [RasPiBrew](https://github.com/steve71/RasPiBrew)
* [ArduinoPi Controller](http://www.fritz-hut.com/arduinopi-v1-5-bluetooth-dongle-support/) - [GitHub](https://github.com/JanStevens/ArduinoPi-Controller)
* [DoctorMonk's blog](http://www.doctormonk.com/2012/04/raspberry-pi-and-arduino.html)
* [FlotCharts](http://flotcharts.org/) - [GitHub](https://github.com/flot/flot)
* [Bootstrap](http://twitter.github.com/bootstrap/index.html)

## Hardware

* [Raspberry Pi](https://www.adafruit.com/products/998) ~$40 (can find them cheaper)
* [Arduino Uno R3](http://www.amazon.com/Arduino-Rev-3-Uno-R3/dp/B006H06TVG/ref=sr_1_1?ie=UTF8&qid=1349220074&sr=8-1&keywords=arduino+uno) ~$25 (can find them cheaper)
* Heating Elements ~$10 each
* Temperature Sensors... I have a few. Going to try the [High Temp Waterproof DS18B20 Digital temperature sensor + extras](https://www.adafruit.com/products/642) from Adafruit ~15 each
* (don't forget the [Food Grade Heat Shrink](https://www.adafruit.com/products/1020) ~$3/foot
* Optional: A wifi dongle for the Raspberry Pi to enable wireless operation ~$15 [I got this one](http://www.amazon.com/AirLink101-AWLL5088-Wireless-Ultra-Adapter/dp/B003X26PMO/ref=sr_1_2?ie=UTF8&qid=1349220458&sr=8-2&keywords=raspberry+pi+wifi)
* Optional: Stainless Steel Electric Ball Valves ~$50 each [I got mine from here](http://www.oscsys.com/store/product/294)
* Optional: 16 channel 12V Relay Board for Arduino (for the Ball Valves) ~$30 [Amazon](http://www.amazon.com/SainSmart-16-Channel-Relay-Module-Arduino/dp/B0057OC66U/ref=sr_1_2?ie=UTF8&qid=1349220222&sr=8-2&keywords=12v+relay+board)
* Optional: A pump. I have two... both purchased on ebay...  One is the standard March pump used in homebrewing.  The other is a Peristaltic pump (which provides suction).  Only need one or the other (if at all).

So, for less than $100 you can be well on your way to a semi-automated brewery with a LOT of expansion options.

## Software

The language for the server side software is Python for rapid development.  The web server/framework is Django.  The site will be developed using the [Bootstrap](http://twitter.github.com/bootstrap/index.html) front-end framework.
On the client side jQuery and various plugins can be used to display data such as line charts and gauges. Mouse overs on the temperature plot will show the time and temp for the individual points.

jQuery and Flot will be used in the client:  
[http://jquery.com](http://jquery.com "jQuery")  
[http://flotcharts.org](http://flotcharts.org)  

The arduino PID libraries will be used.  Other projects have used the C code was from "PID Controller Calculus with full C source source code" by Emile van de Logt
An explanation on how to tune it is from the following web site:  
[http://www.vandelogt.nl/htm/regelen_pid_uk.htm](http://www.vandelogt.nl/htm/regelen_pid_uk.htm)  

The PID can be tuned very simply via the Ziegler-Nichols open loop method.  Just follow the directions in the controller interface screen, highlight the sloped line in the temperature plot and the parameters are automatically calculated.  After tuning with the Ziegler-Nichols method the parameters still needed adjustment because there was an overshoot of about 2 degrees in my system. I did not want the temperature to go past the setpoint since it takes a long time to come back down. Therefore, the parameters were adjusted to eliminate the overshoot.  For this particular system the Ti term was more than doubled and the Td parameter was set to about a quarter of the open loop calculated value.  Also a simple moving average was used on the temperature data that was fed to the PID controller to help improve performance.  Tuning the parameters via the Integral of Time weighted Absolute Error (ITAE-Load) would provide the best results as described on van de Logt's website above.