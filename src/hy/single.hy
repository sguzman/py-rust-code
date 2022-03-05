(import payload [exec])

(defn main []
    (print (exec)))

(if (= __name__ "__main__")
    (main))