# Day 12

## Description
Now it's time to deliver! 🚚

Remember all the orders we received yesterday at the warehouse?

Well... We need to deliver them.

The main problem is that we made a sub-contract for that and there's only one vehicle available... For 443 places to go! 😱

We’ve noticed that going from location A to location B might be different from going from B to A 🔄🚦.

So we need to figure out the best possible path to minimize ⏱️ delivery times.

Can you help me solve this problem? 🧩

[Here you can find an instance of this problem](./instance.txt).

🎯 Challenge time:
Since this is a well-known problem in the literature, let’s make it a mini competition 🎉:

Submit your solution with:
The value of the Objective Function for your path
Your running time 🕒
A link to your code 💻
I’ll collect all submissions in today’s LinkedIn post, and everything will be summarized on this Notion page. I've added modeling language and solver just in case, but if you build a heuristic here I'd write the programming language and the name of the heuristic.
Let's see who rocks it! 🎸

⚠️ Reminder ⚠️

This challenge is about to documenting and sharing so we all can improve the way we think about optimization problems, not about actually solving all the 24 problems in 24 days. Don't feel forced to compete here

## Problem's data

* [instance.txt](./instance.txt)

## Notes

* [ORTools TSP](https://developers.google.com/optimization/routing/tsp)

## Solution

* [day12_cv.py](./day12_cv.py)

## Output
```
n=443
Num nodes = 443
solving...
Solution 0, time= 11.9s, objective= 8,237 (bound= 0)
Solution 1, time= 16.4s, objective= 7,223 (bound= 0)
Solution 2, time= 20.4s, objective= 7,095 (bound= 1,029)
Solution 3, time= 21.5s, objective= 6,900 (bound= 1,029)
Solution 4, time= 26.0s, objective= 6,886 (bound= 1,800)
Solution 5, time= 27.2s, objective= 6,875 (bound= 1,895)
Solution 6, time= 29.7s, objective= 6,812 (bound= 1,895)
Solution 7, time= 30.0s, objective= 5,120 (bound= 1,895)
Solution 8, time= 50.5s, objective= 5,084 (bound= 2,321)
Solution 9, time= 56.8s, objective= 5,058 (bound= 2,321)
Solution 10, time= 57.0s, objective= 3,904 (bound= 2,321)
Solution 11, time= 59.8s, objective= 3,895 (bound= 2,321)
Solution 12, time= 62.4s, objective= 3,883 (bound= 2,321)
Solution 13, time= 71.6s, objective= 3,865 (bound= 2,321)
Solution 14, time= 80.0s, objective= 3,855 (bound= 2,321)
Solution 15, time= 80.8s, objective= 3,847 (bound= 2,321)
Solution 16, time= 82.0s, objective= 3,803 (bound= 2,321)
Solution 17, time= 82.8s, objective= 3,683 (bound= 2,321)
Solution 18, time= 86.1s, objective= 3,672 (bound= 2,422)
Solution 19, time= 88.6s, objective= 3,656 (bound= 2,686)
Solution 20, time= 93.8s, objective= 3,619 (bound= 2,686)
Solution 21, time= 95.5s, objective= 3,408 (bound= 2,686)
Solution 22, time= 99.8s, objective= 3,401 (bound= 2,686)
Solution 23, time=100.0s, objective= 3,175 (bound= 2,686)
Solution 24, time=102.2s, objective= 3,165 (bound= 2,686)
Solution 25, time=105.2s, objective= 3,163 (bound= 2,686)
Solution 26, time=106.3s, objective= 3,162 (bound= 2,686)
Solution 27, time=106.4s, objective= 3,160 (bound= 2,686)
Solution 28, time=108.8s, objective= 3,137 (bound= 2,686)
Solution 29, time=111.0s, objective= 3,119 (bound= 2,699)
Solution 30, time=114.8s, objective= 3,110 (bound= 2,699)
Solution 31, time=117.2s, objective= 2,850 (bound= 2,715)
Solution 32, time=131.9s, objective= 2,842 (bound= 2,719)
Solution 33, time=138.3s, objective= 2,833 (bound= 2,720)
Solution 34, time=153.0s, objective= 2,725 (bound= 2,720)
Solution 35, time=171.8s, objective= 2,724 (bound= 2,720)
Solution 36, time=188.8s, objective= 2,721 (bound= 2,720)
Solution 37, time=200.4s, objective= 2,720 (bound= 2,720)
status: OPTIMAL obj=2,720 bound=2,720 time=204.4
Route: 0 -> 10 -> 400 -> 227 -> 220 -> 90 -> 63 -> 35 -> 128 -> 140 -> 194 -> 91 -> 410 -> 383 -> 292 -> 249 -> 171 -> 322 -> 73 -> 288 -> 168 -> 282 -> 273 -> 26 -> 417 -> 390 -> 330 -> 314 -> 71 -> 350 -> 252 -> 369 -> 113 -> 359 -> 7 -> 198 -> 9 -> 149 -> 152 -> 343 -> 391 -> 22 -> 278 -> 316 -> 346 -> 318 -> 271 -> 405 -> 230 -> 240 -> 296 -> 226 -> 441 -> 241 -> 93 -> 96 -> 308 -> 134 -> 208 -> 229 -> 233 -> 209 -> 95 -> 399 -> 320 -> 299 -> 130 -> 141 -> 159 -> 196 -> 19 -> 216 -> 116 -> 290 -> 260 -> 4 -> 1 -> 58 -> 92 -> 18 -> 46 -> 397 -> 355 -> 68 -> 50 -> 385 -> 67 -> 267 -> 223 -> 338 -> 394 -> 20 -> 432 -> 409 -> 280 -> 14 -> 5 -> 142 -> 97 -> 239 -> 203 -> 79 -> 305 -> 264 -> 255 -> 187 -> 83 -> 402 -> 334 -> 243 -> 291 -> 437 -> 262 -> 186 -> 183 -> 135 -> 284 -> 247 -> 326 -> 293 -> 200 -> 49 -> 429 -> 425 -> 232 -> 210 -> 118 -> 377 -> 319 -> 164 -> 87 -> 156 -> 287 -> 254 -> 270 -> 259 -> 218 -> 221 -> 386 -> 89 -> 411 -> 266 -> 263 -> 231 -> 211 -> 48 -> 103 -> 188 -> 440 -> 306 -> 136 -> 246 -> 347 -> 248 -> 236 -> 193 -> 121 -> 202 -> 176 -> 28 -> 201 -> 384 -> 285 -> 57 -> 340 -> 184 -> 146 -> 29 -> 300 -> 24 -> 415 -> 195 -> 418 -> 412 -> 30 -> 33 -> 395 -> 129 -> 80 -> 37 -> 406 -> 389 -> 426 -> 398 -> 2 -> 189 -> 86 -> 199 -> 251 -> 88 -> 276 -> 101 -> 342 -> 283 -> 272 -> 434 -> 414 -> 178 -> 167 -> 61 -> 16 -> 150 -> 76 -> 286 -> 59 -> 27 -> 309 -> 261 -> 351 -> 82 -> 145 -> 298 -> 250 -> 302 -> 420 -> 111 -> 217 -> 81 -> 315 -> 127 -> 54 -> 353 -> 442 -> 423 -> 422 -> 335 -> 312 -> 393 -> 244 -> 424 -> 363 -> 205 -> 32 -> 307 -> 15 -> 160 -> 84 -> 55 -> 401 -> 380 -> 39 -> 166 -> 3 -> 430 -> 182 -> 374 -> 368 -> 358 -> 281 -> 376 -> 313 -> 181 -> 172 -> 237 -> 361 -> 372 -> 324 -> 206 -> 114 -> 235 -> 212 -> 289 -> 269 -> 301 -> 242 -> 436 -> 6 -> 65 -> 25 -> 155 -> 108 -> 222 -> 396 -> 275 -> 110 -> 356 -> 40 -> 147 -> 77 -> 8 -> 131 -> 224 -> 117 -> 21 -> 31 -> 325 -> 277 -> 165 -> 419 -> 238 -> 204 -> 151 -> 85 -> 137 -> 78 -> 213 -> 294 -> 190 -> 104 -> 102 -> 341 -> 158 -> 105 -> 47 -> 143 -> 11 -> 337 -> 408 -> 169 -> 388 -> 133 -> 42 -> 120 -> 225 -> 331 -> 328 -> 162 -> 94 -> 51 -> 349 -> 332 -> 197 -> 34 -> 407 -> 154 -> 303 -> 153 -> 175 -> 268 -> 234 -> 43 -> 99 -> 367 -> 354 -> 191 -> 163 -> 279 -> 357 -> 258 -> 245 -> 70 -> 371 -> 38 -> 421 -> 438 -> 336 -> 60 -> 12 -> 317 -> 378 -> 344 -> 41 -> 66 -> 44 -> 404 -> 311 -> 323 -> 119 -> 144 -> 339 -> 392 -> 69 -> 433 -> 428 -> 381 -> 180 -> 64 -> 352 -> 360 -> 106 -> 348 -> 366 -> 179 -> 126 -> 125 -> 52 -> 177 -> 375 -> 56 -> 387 -> 185 -> 253 -> 207 -> 75 -> 427 -> 265 -> 256 -> 157 -> 23 -> 274 -> 373 -> 304 -> 36 -> 370 -> 362 -> 45 -> 148 -> 295 -> 170 -> 112 -> 53 -> 435 -> 13 -> 364 -> 382 -> 257 -> 72 -> 74 -> 228 -> 214 -> 100 -> 297 -> 192 -> 333 -> 109 -> 107 -> 173 -> 379 -> 161 -> 138 -> 439 -> 403 -> 365 -> 329 -> 215 -> 416 -> 115 -> 139 -> 132 -> 219 -> 327 -> 310 -> 17 -> 124 -> 122 -> 321 -> 123 -> 345 -> 62 -> 174 -> 98 -> 431 -> 413 -> 0
Travelled distance: 2720
```
