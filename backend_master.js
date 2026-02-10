/* BACKEND MASTER: Progression Logic */
export const MasterConfig = {
    // Defined Tiers for the Map
    levels: [
        {
            id: "beginner",
            title: "THE VALLEY OF INITIATES",
            playlists: ["PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF", "PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi", "PL8dPuuaLjXtO65LeD2p4_Sb5XQ51par_b"]
        },
        {
            id: "intermediate",
            title: "THE PEAKS OF PERCEPTION",
            playlists: ["PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI", "PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s", "PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU"]
        },
        {
            id: "advanced",
            title: "THE SUMMIT OF MASTERY",
            playlists: ["PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI", "PLoROMvodv4rNyWOpJg_Yh4NSqI4Z4vOYy"]
        }
    ],

    // Detailed Metadata
    modules: {
        // Beginner
        "PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF": { title: "StatQuest Archives", description: "Statistical foundations." },
        "PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi": { title: "3B1B Neural Hub", description: "Visualizing calculus." },
        "PL8dPuuaLjXtO65LeD2p4_Sb5XQ51par_b": { title: "CrashCourse AI", description: "History & Ethics." },
        
        // Intermediate
        "PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI": { title: "Andrew Ng's Dojo", description: "Deep Learning Specialization." },
        "PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s": { title: "FreeCodeCamp Labs", description: "Applied TensorFlow." },
        "PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU": { title: "Deeplizard PyTorch", description: "Neural Frameworks." },
        
        // Advanced
        "PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI": { title: "MIT 6.S191", description: "State of the Art AGI." },
        "PLoROMvodv4rNyWOpJg_Yh4NSqI4Z4vOYy": { title: "Stanford CS229", description: "Mathematical Rigor." }
    }
};

export const UserPersona = {
    getProfile: () => ({ name: "Abhijay Pandey", university: "Galgotias University" }),
    getGreeting: () => `Maester Abhijay | Galgotias Sector`
};

export const Evaluation = {
    process: (score, total) => {
        const pct = Math.round((score / total) * 100);
        return { passed: pct >= 60, pct: pct };
    }
};

export const ProgressLogic = {
    save: (id) => {
        const current = JSON.parse(localStorage.getItem('edu_comp') || "[]");
        if(!current.includes(id)) {
            current.push(id);
            localStorage.setItem('edu_comp', JSON.stringify(current));
        }
    }
};