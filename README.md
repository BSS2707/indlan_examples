# IndLan

> A Programming Language for India — Code in Hindi, English, or Both.

IndLan (Indian Language) is a programming language designed to make coding more natural and accessible for Indian programmers. It supports both English and Hindi-inspired keywords, allowing developers to write programs in the language style they prefer.

🌐 Website: [www.indlan.me](http://www.indlan.me)

---

## Features

* Hindi and English keywords
* Mix both languages in the same program
* Variables and data types
* Conditions
* While, for-each, and do-while loops
* Functions and return values
* Object-oriented programming with classes
* Switch statements
* User input functions
* F-Strings
* Mathematical built-ins
* String and list methods
* Exponentiation operator
* Desktop IDE
* `.ind` file support
* Interactive REPL

---

# Installation

Install IndLan using pip:

```bash
pip install indlan
```

Run an IndLan file:

```bash
indlan program.ind
```

Start the interactive REPL:

```bash
indlan
```

Launch the IndLan IDE:

```bash
indlan-ide
```

---

# Hello World

### Hindi Style

```indlan
chhap("IndLan se Namaste!")
```

### English Style

```indlan
print("Hello from IndLan!")
```

---

# Variables

Variables can be declared using Hindi or English keywords.

```indlan
maano naam = "Bhavya"
maano umar = 20
maano score = 98.5

chhap(naam)
chhap(umar)
chhap(score)
```

English:

```indlan
let name = "Bhavya"
let age = 20

print(name)
print(age)
```

---

# Conditions

```indlan
maano score = 75

agar score >= 90 {
    chhap("Grade A")
} nahito_agar score >= 75 {
    chhap("Grade B")
} nahito_agar score >= 50 {
    chhap("Grade C")
} nahito {
    chhap("Failed")
}
```

English:

```indlan
let score = 75

if score >= 90 {
    print("Grade A")
} elif score >= 75 {
    print("Grade B")
} else {
    print("Failed")
}
```

---

# While Loop

```indlan
maano i = 1

jabtak i <= 5 {
    chhap(i)
    i += 1
}
```

Output:

```text
1
2
3
4
5
```

---

# For Loop

```indlan
pratyek number mein range(5) {
    chhap(number)
}
```

English:

```indlan
for number in range(5) {
    print(number)
}
```

---

# Functions

```indlan
kaam jodo(a, b) {
    vapas a + b
}

maano result = jodo(10, 20)

chhap(result)
```

English:

```indlan
fun add(a, b) {
    return a + b
}

print(add(10, 20))
```

---

# F-Strings

```indlan
maano naam = "Bhavya"
maano umar = 20

chhap(f"Namaste {naam}!")
chhap(f"Aapki umar {umar} saal hai.")
```

Expressions can also be used:

```indlan
maano number = 10

chhap(f"Square: {number ** 2}")
```

---

# User Input

```indlan
maano naam = aalao("Aapka naam kya hai? ")
maano umar = number_dalao("Aapki umar kya hai? ")

chhap(f"Namaste {naam}!")
chhap(f"Aap {umar} saal ke hain.")
```

English input functions:

```indlan
let name = input("Enter your name: ")
let age = input_int("Enter your age: ")

print(f"Hello {name}")
```

---

# Classes

```indlan
varg Player {

    kaam init(naam, rating) {
        yeh.naam = naam
        yeh.rating = rating
    }

    kaam profile() {
        chhap(f"Player: {yeh.naam}")
        chhap(f"Rating: {yeh.rating}")
    }

}

maano player = naya Player("Bhavya", 2088)

player.profile()
```

---

# Switch Statement

```indlan
maano din = 3

vibhag din {

    sthiti 1 {
        chhap("Monday")
    }

    sthiti 2 {
        chhap("Tuesday")
    }

    sthiti 3 {
        chhap("Wednesday")
    }

    anyatha {
        chhap("Unknown Day")
    }

}
```

---

# Do While Loop

```indlan
maano i = 0

karo {
    chhap(i)
    i += 1
} jabtak i < 5
```

---

# Lists

```indlan
maano numbers = [10, 20, 30, 40]

chhap(numbers)
chhap(numbers[-1])

numbers.append(50)

chhap(numbers)
```

---

# String Methods

```indlan
maano text = "hello indlan"

chhap(text.upper())
chhap(text.lower())
chhap(text.replace("indlan", "world"))
```

---

# Mathematical Functions

```indlan
chhap(sqrt(144))
chhap(abs(-42))
chhap(max(10, 20, 30))
chhap(min(10, 20, 30))
chhap(round(3.14159, 2))
```

---

# Keyword Reference

| English    | Hindi         | Purpose        |
| ---------- | ------------- | -------------- |
| `let`      | `maano`       | Variable       |
| `if`       | `agar`        | Condition      |
| `elif`     | `nahito_agar` | Else If        |
| `else`     | `nahito`      | Else           |
| `while`    | `jabtak`      | While Loop     |
| `for`      | `pratyek`     | For Loop       |
| `in`       | `mein`        | Membership     |
| `fun`      | `kaam`        | Function       |
| `return`   | `vapas`       | Return         |
| `class`    | `varg`        | Class          |
| `new`      | `naya`        | Create Object  |
| `this`     | `yeh`         | Current Object |
| `break`    | `roko`        | Break          |
| `continue` | `jaari`       | Continue       |
| `true`     | `sahi`        | Boolean True   |
| `false`    | `galat`       | Boolean False  |
| `null`     | `khaali`      | Null           |
| `switch`   | `vibhag`      | Switch         |
| `case`     | `sthiti`      | Case           |
| `default`  | `anyatha`     | Default        |

---

# Example Program

A complete simple program:

```indlan
maano naam = aalao("Aapka naam: ")
maano score = number_dalao("Aapka score: ")

agar score >= 90 {
    chhap(f"Bahut badhiya {naam}! Grade A")
} nahito_agar score >= 75 {
    chhap(f"Good job {naam}! Grade B")
} nahito_agar score >= 50 {
    chhap(f"Keep improving {naam}! Grade C")
} nahito {
    chhap(f"Practice more {naam}!")
}
```

---

# How IndLan Works

IndLan uses a tree-walking interpreter architecture:

```text
IndLan Source Code (.ind)
            ↓
          Lexer
            ↓
          Parser
            ↓
            AST
            ↓
       Interpreter
            ↓
          Output
```

---

# Project Structure

```text
IndLan/
│
├── lexer.py
├── ind_parser.py
├── ast_nodes.py
├── interpreter.py
├── indlan.py
├── indlan_ide.py
│
├── examples/
│   ├── hello.ind
│   ├── variables.ind
│   ├── loops.ind
│   ├── functions.ind
│   └── classes.ind
│
└── README.md
```

---

# Why IndLan?

Many Indian students first think about programming logic in Hindi or their native language, but traditional programming languages require English keywords.

IndLan reduces this barrier.

Instead of:

```javascript
if age > 18 {
    print("Adult")
}
```

You can write:

```indlan
agar umar > 18 {
    chhap("Adult")
}
```

Or even mix both styles:

```indlan
maano age = 20

if age >= 18 {
    chhap("You are eligible!")
}
```

---

# Vision

IndLan aims to make programming more accessible and natural for Indian learners by allowing them to code using familiar Hindi-inspired keywords without losing the power of modern programming concepts.

**Think in Hindi. Code in IndLan.**

---

## Creator

**Bhavya S Solanki**

Creator of IndLan Programming Language

🌐 [www.indlan.me](http://www.indlan.me)

Made in India 🇮🇳
