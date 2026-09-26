// PostHog and Sentry load only when their keys are set, so the site works without them.
const env = import.meta.env;
let ph: typeof import('posthog-js').default | null = null;

export async function initTelemetry() {
  if (env.PUBLIC_SENTRY_DSN) {
    const Sentry = await import('@sentry/browser');
    Sentry.init({ dsn: env.PUBLIC_SENTRY_DSN });
  }
  if (env.PUBLIC_POSTHOG_KEY) {
    ph = (await import('posthog-js')).default;
    ph.init(env.PUBLIC_POSTHOG_KEY, {
      api_host: env.PUBLIC_POSTHOG_HOST || 'https://us.i.posthog.com',
      capture_pageview: true,
      person_profiles: 'identified_only',
      persistence: 'localStorage',
    });
  }
}

export function track(event: string, props: Record<string, string>) {
  ph?.capture(event, props);
}
