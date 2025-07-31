(ns reverse-string)

(defn reverse-string [string-to-reverse]
  (apply str (reverse string-to-reverse))
)
