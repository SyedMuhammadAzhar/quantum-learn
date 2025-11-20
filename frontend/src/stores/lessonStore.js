import { writable, derived } from 'svelte/store';

// Define all available lessons
export const lessons = {
    superposition: {
        id: 'superposition',
        title: 'Superposition',
        subtitle: 'One thing, many states',
        icon: '🪙',
        color: '#667eea',
        steps: [
            {
                id: 'intro',
                title: 'Welcome to Quantum World',
                type: 'intro'
            },
            {
                id: 'classical',
                title: 'Classical vs Quantum',
                type: 'explanation'
            },
            {
                id: 'analogy',
                title: 'The Spinning Coin',
                type: 'analogy'
            },
            {
                id: 'math',
                title: 'The Math (Made Simple)',
                type: 'math'
            },
            {
                id: 'demo',
                title: 'Try It Yourself!',
                type: 'demo'
            },
            {
                id: 'faq',
                title: 'FAQ',
                type: 'faq'
            }
        ]
    },
    entanglement: {
        id: 'entanglement',
        title: 'Entanglement',
        subtitle: 'Spooky action at a distance',
        icon: '🔗',
        color: '#e74c3c',
        steps: [],
        locked: true
    },
    measurement: {
        id: 'measurement',
        title: 'Measurement',
        subtitle: 'Observing changes reality',
        icon: '👁️',
        color: '#27ae60',
        steps: [],
        locked: true
    }
};

// Current lesson state
function createLessonStore() {
    const { subscribe, set, update } = writable({
        currentLessonId: null,
        currentStepIndex: 0,
        completedLessons: [],
        completedSteps: {},
    });

    return {
        subscribe,
        
        startLesson: (lessonId) => update(state => ({
            ...state,
            currentLessonId: lessonId,
            currentStepIndex: 0
        })),
        
        nextStep: () => update(state => {
            const lesson = lessons[state.currentLessonId];
            if (!lesson) return state;
            
            const newIndex = Math.min(state.currentStepIndex + 1, lesson.steps.length - 1);
            
            const currentStep = lesson.steps[state.currentStepIndex];
            const lessonSteps = state.completedSteps[state.currentLessonId] || [];
            
            if (!lessonSteps.includes(currentStep.id)) {
                lessonSteps.push(currentStep.id);
            }
            
            return {
                ...state,
                currentStepIndex: newIndex,
                completedSteps: {
                    ...state.completedSteps,
                    [state.currentLessonId]: lessonSteps
                }
            };
        }),
        
        previousStep: () => update(state => ({
            ...state,
            currentStepIndex: Math.max(state.currentStepIndex - 1, 0)
        })),
        
        goToStep: (index) => update(state => ({
            ...state,
            currentStepIndex: index
        })),
        
        completeLesson: () => update(state => {
            const completedLessons = state.completedLessons.includes(state.currentLessonId)
                ? state.completedLessons
                : [...state.completedLessons, state.currentLessonId];
            
            return {
                ...state,
                completedLessons
            };
        }),
        
        exitLesson: () => update(state => ({
            ...state,
            currentLessonId: null,
            currentStepIndex: 0
        })),
        
        reset: () => set({
            currentLessonId: null,
            currentStepIndex: 0,
            completedLessons: [],
            completedSteps: {}
        })
    };
}

export const lessonStore = createLessonStore();

// Derived store for current lesson info
export const currentLesson = derived(lessonStore, ($store) => {
    if (!$store.currentLessonId) return null;
    return lessons[$store.currentLessonId];
});

// Derived store for current step
export const currentStep = derived(
    [lessonStore, currentLesson],
    ([$store, $lesson]) => {
        if (!$lesson) return null;
        return $lesson.steps[$store.currentStepIndex];
    }
);

// Derived store for progress percentage
export const lessonProgress = derived(
    [lessonStore, currentLesson],
    ([$store, $lesson]) => {
        if (!$lesson || $lesson.steps.length === 0) return 0;
        return Math.round((($store.currentStepIndex + 1) / $lesson.steps.length) * 100);
    }
);