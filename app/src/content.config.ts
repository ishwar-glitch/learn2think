import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Reads ../content. Batch P3 replaces these loose schemas with per-template (T1-T10) schemas.
const loose = z.object({}).passthrough();
const md = (dir: string) => glob({ pattern: '**/*.md', base: `../content/${dir}` });

export const collections = {
  universe: defineCollection({ loader: md('universe'), schema: loose }),
  core: defineCollection({ loader: md('core'), schema: loose }),
  specialist: defineCollection({ loader: md('specialist'), schema: loose }),
  cases: defineCollection({ loader: md('cases'), schema: loose }),
  interview: defineCollection({ loader: md('interview'), schema: loose }),
  labs: defineCollection({ loader: md('labs'), schema: loose }),
  taxonomy: defineCollection({ loader: md('taxonomy'), schema: loose }),
};
