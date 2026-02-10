/* MASTER ARCHIVE: All 3 Levels of Machine Learning */

const courseDB = {
    // --- LEVEL 1: BEGINNER (The Valley) ---
    "PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF": [ // StatQuest
        { title: "Introduction to Machine Learning", id: "Gv9_4yMHFhI" },
        { title: "Cross Validation", id: "fSytzGwwBVw" },
        { title: "The Confusion Matrix", id: "Kdsp6soqA7o" },
        { title: "Bias and Variance", id: "EuBBz3bI-aA" }
    ],
    "PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi": [ // 3Blue1Brown
        { title: "But what is a Neural Network?", id: "aircAruvnKk" },
        { title: "Gradient descent", id: "IHZwWFHWa-w" },
        { title: "What is backpropagation?", id: "Ilg3gGewQ5U" }
    ],
    "PL8dPuuaLjXtO65LeD2p4_Sb5XQ51par_b": [ // CrashCourse AI
        { title: "What is AI?", id: "JMUxmLyrhSk" },
        { title: "Neural Networks", id: "bfmFfD2RIcg" },
        { title: "Algorithmic Bias", id: "BrM_L416Yxs" }
    ],

    // --- LEVEL 2: INTERMEDIATE (The Peaks) ---
    "PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI": [ // Andrew Ng
        { title: "Welcome to Deep Learning", id: "0QLrLe85msM" },
        { title: "Neural Network Basics", id: "PPLop4lL2eI" },
        { title: "Vectorization", id: "qsIrQi0fzbY" }
    ],
    "PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s": [ // FreeCodeCamp
        { title: "Machine Learning for Everybody", id: "i_LwzRVP7bg" },
        { title: "TensorFlow 2.0 Complete Course", id: "tPYj3fFJGjk" }
    ],
    "PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU": [ // Deeplizard
        { title: "PyTorch Explained", id: "v5cngxo4mIg" },
        { title: "CUDA and GPU", id: "6stDkxY8Q8M" }
    ],

    // --- LEVEL 3: ADVANCED (The Summit) ---
    "PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI": [ // MIT 6.S191
        { title: "Intro to Deep Learning", id: "5tvmMX8r_OM" },
        { title: "Deep Sequence Modeling", id: "qPoO1F4VItM" }
    ],
    "PLoROMvodv4rNyWOpJg_Yh4NSqI4Z4vOYy": [ // Stanford CS229
        { title: "Lecture 1: Introduction", id: "jGwO_UgTS7I" },
        { title: "Lecture 2: Linear Regression", id: "4b4MUYve_U8" },
        { title: "Lecture 3: Locally Weighted Regression", id: "HetCRoY6q6E" }
    ]
};

// --- EXAM LOGIC ---
const finalQuestionBank = [
    { case: "THEORY", q: "Which algorithm minimizes the cost function?", options: ["Gradient Descent", "Random Forest", "K-Means"], correct: 0 },
    { case: "MATH", q: "What is the derivative of the Sigmoid function?", options: ["f(x)(1-f(x))", "1/x", "x^2"], correct: 0 },
    { case: "ETHICS", q: "Overfitting occurs when...", options: ["Model learns noise", "Model is too simple", "Data is corrupted"], correct: 0 },
    { case: "CODE", q: "Which library is used for Tensors?", options: ["PyTorch", "React", "Flask"], correct: 0 },
    { case: "ARCH", q: "What does CNN stand for?", options: ["Convolutional Neural Network", "Central Network Node", "Computer Neural Net"], correct: 0 }
];

// --- HELPER FUNCTIONS ---
function getTopicSummary(title) {
    return {
        abstract: "The Maesters have documented this phenomenon. It involves optimizing weights to reduce error."
    };
}

function getTopicQuestions(title, idx) {
    return {
        q1: "True or False: A lower loss value is better.",
        a1: "True",
        w1: "False"
    };
}