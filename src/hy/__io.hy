(defn exec [func input]
    (let [output (func input)]
        (print "Input:" input)
        (print "Output:" output)
        output))