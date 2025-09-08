const API_KEY = 'skskkskskksksksksk';

function slowArrayProcessing(arr) {
    let result = [];
    for (var i = 0; i < arr.length; i++) {  // Should use let/const instead of var
        for (var j = 0; j < arr.length; j++) {  // O(n²) complexity
            if (arr[i] == arr[j]) {  // Should use === instead of ==
                result.push(arr[i]);
            }
        }
    }
    return result;
}

// Security issue: XSS vulnerability
function displayUserContent(userInput) {
    document.getElementById('content').innerHTML = userInput;  // Dangerous!
}

// Security issue: eval usage
function executeCode(code) {
    return eval(code);  // Very dangerous!
}

// Complexity issue: deeply nested conditions
function complexLogic(a, b, c, d, e) {
    if (a > 0) {
        if (b > 0) {
            if (c > 0) {
                if (d > 0) {
                    if (e > 0) {
                        return 'all positive';
                    } else {
                        return 'e not positive';
                    }
                } else {
                    return 'd not positive';
                }
            } else {
                return 'c not positive';
            }
        } else {
            return 'b not positive';
        }
    } else {
        return 'a not positive';
    }
}

// Documentation issue: missing JSDoc
function undocumentedFunction(param1, param2) {
    return param1 + param2;
}

// Code duplication
function validateEmail(email) {
    if (!email) {
        throw new Error('Email is required');
    }
    if (typeof email !== 'string') {
        throw new Error('Email must be a string');
    }
    return email.includes('@');
}

function validateUsername(username) {
    if (!username) {
        throw new Error('Username is required');  // Duplicated validation pattern
    }
    if (typeof username !== 'string') {
        throw new Error('Username must be a string');  // Duplicated validation pattern
    }
    return username.length > 3;
}

// Performance issue: string concatenation in loop
function buildMessage(items) {
    let message = '';
    for (let i = 0; i < items.length; i++) {
        message += items[i] + ', ';  // Inefficient for large arrays
    }
    return message;
}

// Best practice issue: callback hell
function fetchUserData(userId, callback) {
    fetch(`/api/users/${userId}`)
        .then(response => {
            response.json().then(user => {
                fetch(`/api/posts/${user.id}`)
                    .then(response => {
                        response.json().then(posts => {
                            fetch(`/api/comments/${posts[0].id}`)
                                .then(response => {
                                    response.json().then(comments => {
                                        callback(null, { user, posts, comments });
                                    });
                                });
                        });
                    });
            });
        })
        .catch(error => {
            callback(error);
        });
}

// Security issue: dangerous setTimeout usage
function delayedExecution(code, delay) {
    setTimeout(code, delay);  // String-based setTimeout is dangerous
}

// Missing error handling
function divideNumbers(a, b) {
    return a / b;  // No check for division by zero
}

// Long function (maintainability issue)
function processUserDataAndGenerateReport(users) {
    // This function is too long and does too many things
    let processedUsers = [];
    
    for (let i = 0; i < users.length; i++) {
        let user = users[i];
        
        // Validate user
        if (!user.name || !user.email) {
            continue;
        }
        
        // Process user data
        user.name = user.name.trim().toLowerCase();
        user.email = user.email.trim().toLowerCase();
        
        // Calculate user score
        let score = 0;
        if (user.posts && user.posts.length > 0) {
            score += user.posts.length * 10;
        }
        if (user.comments && user.comments.length > 0) {
            score += user.comments.length * 5;
        }
        if (user.likes && user.likes.length > 0) {
            score += user.likes.length * 2;
        }
        
        user.score = score;
        processedUsers.push(user);
    }
    
    // Sort users by score
    processedUsers.sort((a, b) => b.score - a.score);
    
    // Generate report
    let report = {
        totalUsers: processedUsers.length,
        topUsers: processedUsers.slice(0, 10),
        averageScore: processedUsers.reduce((sum, user) => sum + user.score, 0) / processedUsers.length
    };
    
    return report;
}

// Class without proper documentation
class UndocumentedClass {
    constructor(value) {
        this.value = value;
    }
    
    methodWithoutDocumentation() {
        return this.value * 2;
    }
}

// Global variable pollution
var globalVariable = 'This should not be global';

// Example usage
console.log(slowArrayProcessing([1, 2, 3, 2, 1]));
console.log(complexLogic(1, 2, 3, 4, 5));
console.log(undocumentedFunction(5, 10));
