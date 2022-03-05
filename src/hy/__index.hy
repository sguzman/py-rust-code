(defn exec [list]
    (fn [n] (get list n)))