(import __arg          [exec :as arg])
(import __file_to_text [exec :as text])
(import __slurp        [exec :as slurp])
(import __init      [exec :as compose])


(defn exec []
    (setv a (arg))
    (print a)
    (setv t (text a))
    (setv s (slurp t))
    (print (. s uscDoc)))