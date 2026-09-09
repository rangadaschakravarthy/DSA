"""
Level 9: Parse Lisp Expression

Problem:
Evaluate a Lisp-like expression. The expression is given as a string, which may contain:
- Integer literals (e.g. "12", "-3")
- Variables
- Expressions:
  - `(let v1 e1 v2 e2 ... vn en expr)`: assign e1 to v1, etc., then evaluate expr.
  - `(add e1 e2)`: evaluates e1 + e2.
  - `(mult e1 e2)`: evaluates e1 * e2.

Time Complexity: O(N^2)
Space Complexity: O(N) scope environments stack
"""

def evaluate(expression: str) -> int:
    def parse_tokens(expr):
        tokens = []
        i = 0
        n = len(expr)
        while i < n:
            if expr[i] == ' ':
                i += 1
            elif expr[i] == '(':
                count = 1
                start = i
                i += 1
                while i < n and count > 0:
                    if expr[i] == '(':
                        count += 1
                    elif expr[i] == ')':
                        count -= 1
                    i += 1
                tokens.append(expr[start:i])
            else:
                start = i
                while i < n and expr[i] != ' ' and expr[i] != ')':
                    i += 1
                tokens.append(expr[start:i])
        return tokens

    def helper(expr, scope):
        if not expr.startswith('('):
            if expr in scope:
                return scope[expr]
            return int(expr)

        # Remove outer parentheses
        inner = expr[1:-1]
        tokens = parse_tokens(inner)
        command = tokens[0]

        if command == 'add':
            return helper(tokens[1], scope) + helper(tokens[2], scope)
        elif command == 'mult':
            return helper(tokens[1], scope) * helper(tokens[2], scope)
        elif command == 'let':
            new_scope = dict(scope)
            for i in range(1, len(tokens) - 1, 2):
                var = tokens[i]
                val = helper(tokens[i + 1], new_scope)
                new_scope[var] = val
            return helper(tokens[-1], new_scope)

    return helper(expression, {})


if __name__ == "__main__":
    assert evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))") == 14
    assert evaluate("(let x 3 x 2 x)") == 2
    assert evaluate("(let a1 3 b2 (add a1 1) (mult a1 b2))") == 12
    print("[PASS] Level 9 Parse Lisp Expression tests passed!")
