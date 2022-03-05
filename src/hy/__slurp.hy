(import functools [cache :as c])

(import untangle [parse :as p])

(with-decorator c
    (defn exec [text]
        (p text)))