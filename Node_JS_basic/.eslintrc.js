module.exports = {
    env: {
        browser: false,
        es6: true,
        jest: true,
        node: true,
    },
    extends: ['eslint:recommended'],
    globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
    },
    parserOptions: {
        ecmaVersion: 2018,
        sourceType: 'module',
    },
    rules: {
        indent: ['error', 2],
        'linebreak-style': ['error', 'unix'],
        quotes: ['error', 'single'],
        semi: ['error', 'always'],
    },
};
