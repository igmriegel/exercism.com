module LuciansLusciousLasagna


let expectedMinutesInOven: int = 40

let remainingMinutesInOven (actualTime: int) = expectedMinutesInOven - actualTime

let preparationTimeInMinutes (numLayers: int) = 2 * numLayers

let elapsedTimeInMinutes (numLayers: int) (actualTime: int) = preparationTimeInMinutes numLayers + actualTime