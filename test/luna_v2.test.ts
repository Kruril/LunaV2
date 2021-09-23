import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as LunaV2 from '../lib/luna_v2-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new LunaV2.LunaV2Stack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
