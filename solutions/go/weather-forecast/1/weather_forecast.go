// Package weather
//
// Package implements a forecast function to provide a weather forecast.
package weather

// CurrentCondition represents the weather condition.
var CurrentCondition string
// CurrentLocation represents the location for the forecast.
var CurrentLocation string

// Forecast Returns a string with the weather forecast.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
