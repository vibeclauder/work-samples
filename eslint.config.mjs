import { defineConfig, globalIgnores } from 'eslint/config';
import next from 'eslint-config-next';

const config = defineConfig([
  ...next,
  globalIgnores(['node_modules/**', '.next/**', 'out/**', 'next-env.d.ts', 'public/**']),
]);

export default config;
