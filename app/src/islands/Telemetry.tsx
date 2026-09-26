import { useEffect } from 'react';
import { initTelemetry } from '../lib/telemetry';

export default function Telemetry() {
  useEffect(() => { initTelemetry().catch(() => {}); }, []);
  return null;
}
