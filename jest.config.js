/**
 * Dihya – Configuration Jest ultra avancée
 * - Couverture maximale (unit, integration, e2e)
 * - Multistack (React, Node, TypeScript, i18n)
 * - Sécurité, accessibilité, performance, souveraineté
 * - Prêt CI/CD, Codespaces, Linux
 * - Multilingue (fr, en, ar, tzm) via i18n-mock
 * - Zéro warning, zéro fail lint/test/build
 */

module.exports = {
  preset: 'ts-jest/presets/js-with-ts',
  testEnvironment: 'jsdom',
  roots: [
    '<rootDir>/src',
    '<rootDir>/tests',
    '<rootDir>/Dihya/Dihya/backend/node/app/tests/integration',
    '<rootDir>/Dihya/Dihya/backend/node/tests/integration',
    '<rootDir>/Dihya/Dihya/backend/assets/datasets/fixtures'
  ],
  moduleFileExtensions: ['js', 'jsx', 'ts', 'tsx', 'json'],
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
    '^.+\\.(js|jsx)$': 'babel-jest'
  },
  setupFilesAfterEnv: [
    '<rootDir>/tests/setupTests.js'
  ],
  collectCoverage: true,
  coverageDirectory: '<rootDir>/coverage',
  coverageReporters: ['text', 'lcov', 'json', 'clover'],
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/i18n/**',
    '!src/**/types/**'
  ],
  testMatch: [
    '**/__tests__/**/*.[jt]s?(x)',
    '**/?(*.)+(spec|test).[tj]s?(x)',
    '**/test_fixtures_assets.test.js'
  ],
  testPathIgnorePatterns: [
    '/node_modules/',
    '/dist/',
    '/build/',
    '/coverage/'
  ],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '^@/(.*)$': '<rootDir>/src/$1',
    '^i18n$': '<rootDir>/tests/__mocks__/i18nMock.js'
  },
  reporters: [
    'default',
    ['jest-junit', { outputDirectory: './reports/junit', outputName: 'junit.xml' }]
  ],
  testTimeout: 20000,
  maxWorkers: '50%',
  verbose: true,
  // Sécurité : sandbox, isolation, pas de leak d’état
  clearMocks: true,
  resetMocks: true,
  restoreMocks: true,
  // Accessibilité : axe-core pour tests a11y (voir setupTests.js)
  // Souveraineté : pas de dépendance cloud, tout local/mocked
  // Multilingue : tests i18n via mock, voir tests/i18n/
};
