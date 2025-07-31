(ns tracks-on-tracks-on-tracks)

(defn new-list
  []
  '()
  )

(defn add-language
  [lang-list lang]
  (cons lang lang-list)
  )

(defn first-language
  [lang-list]
  (first lang-list)
  )

(defn remove-language
  [lang-list]
  (pop lang-list)
  )

(defn count-languages
  [lang-list]
  (count lang-list)
  )

(defn learning-list
  []
  (def mylist (conj (conj (pop (conj (conj (list) "Clojure") "Lisp")) "Java") "JavaScript"))
  (count mylist)
  )
