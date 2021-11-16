#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { LunaV2Stack } from '../lib/luna_v2-stack';

const app = new cdk.App();
new LunaV2Stack(app, 'LunaV2Stack', {});
