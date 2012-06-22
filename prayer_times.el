;; Copyright 2012 Cory Koch
;;
;; This file is part of PrayerTimes.
;;
;; PrayerTimes is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; PrayerTimes is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with PrayerTimes.  If not, see <http://www.gnu.org/licenses/>.
;;
;; ********************************************************************
;;  
;; Usage: TODO:
;; 
;; Configuration: TODO: write script to use wget to retrieve prayer times 
;;
;; All prayer times are taken from islamicfinder.org



(defun getPrayerTimes ()
  "Get prayer times for the current date"
  (setq month (format-time-string "%m")
       day (format-time-string "%d")
       year (format-time-string "%Y")
       (message "Todays date is %s" month)
       ))
  (getPrayerTimes)

(defun parseXML ()
  "Convert xml to lisp data struct"
  (let ))

 (defun getDate ()
    "get the date a month, day, year"
    (setq date (format-time-string "%m-%d-%Y")))

;; Get month
(with-temp-buffer
      (insert (getDate))
      (buffer-substring 1 3))
;; Get day
(with-temp-buffer
      (insert (getDate))
      (buffer-substring 4 6))
;; Get year
(with-temp-buffer
      (insert (getDate))
      (buffer-substring 7 11))



(setq x (getDate))

(setq x (+ 1 1 ))