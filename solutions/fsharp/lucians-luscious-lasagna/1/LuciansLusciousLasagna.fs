module LuciansLusciousLasagna

// TODO: define the 'expectedMinutesInOven' binding
let expectedMinutesInOven: int = 40
// TODO: define the 'remainingMinutesInOven' function
let remainingMinutesInOven (actualTime: int) = expectedMinutesInOven - actualTime
// TODO: define the 'preparationTimeInMinutes' function
let preparationTimeInMinutes (numLayers: int) = 2 * numLayers
// TODO: define the 'elapsedTimeInMinutes' function
let elapsedTimeInMinutes (numLayers: int) (actualTime: int) = preparationTimeInMinutes numLayers + actualTime