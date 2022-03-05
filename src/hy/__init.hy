(import __index [exec :as idx])
(import __len [exec :as l])
(import __io [exec :as io])

(defn exec [funcs]
    (let [g (idx funcs)]
        (cond
            [(l funcs 0)
                (fn [x] x)]
            [(l funcs 1)
                (g 0)]
            [(l funcs 2)
                (fn [x]
                    ((g 0) ((g 1) x)))]
            [(fn [x]
                ((g 0) ((g 1)
                (exec
                    (cut funcs 2 (len funcs))))))])))