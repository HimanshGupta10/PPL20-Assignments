
;factorial with recursion
(defun factorialr (num)
   (cond ((zerop num) 1)
      (t ( * num (factorialr (- num 1))))
   )
)

(write-line "Enter the number whose factorial is to be found: ")

;reading the number
(setq n (read))

;printing factorial using recursion
(format t "~% Factorial with recursion of ~d is: ~d" n (factorialr n))
(terpri)

;factorial without recursion
(defun factorialwr (num)
        (setq n num)
        (loop
                (setq n (- n 1))
                (setq num (* num n))
                (when (= n 1) (return num))
        )
)

;printing factorial without recursion
(format t "~% Factorial without recursion of ~d is: ~d" n (factorialwr n))
