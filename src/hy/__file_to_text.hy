(import functools [cache :as c])

(with-decorator c
    (defn exec [filename]
        (let [fs (open filename)]
            (.read fs))))