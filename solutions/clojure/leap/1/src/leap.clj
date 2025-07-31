(ns leap)

(defn evenly-div [x y]
  (zero? (rem x y)))

(defn leap-year? [year]
   (and (evenly-div year 4)(or (not (evenly-div year 100))(evenly-div year 400)))
)
