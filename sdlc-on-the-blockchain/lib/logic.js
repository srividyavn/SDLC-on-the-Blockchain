/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Sample transaction processor function.
 * @param {org.acme.howto.ChangeStateToProduction} tx The transaction that changes the state of the order from to the production state.
 * @transaction
 */

function ChangeStateToProduction(tx) {

tx.order.state = "production";
  
    // Get the asset registry for the order asset.
    return getAssetRegistry('org.acme.howto.Order')
        .then(function (assetRegistry) {

            // Update the asset in the order asset registry.
            return assetRegistry.update(tx.order);
        });
}

/**
 * Sample transaction processor function.
 * @param {org.acme.howto.ChangeStateToDevelopment} tx The transaction that changes the state of the order from to the development state.
 * @transaction
 */

function ChangeStateToDevelopment(tx) {

tx.order.state = "development";
  
    // Get the asset registry for the order asset.
    return getAssetRegistry('org.acme.howto.Order')
        .then(function (assetRegistry) {

            // Update the asset in the order asset registry.
            return assetRegistry.update(tx.order);
        });
}

/**
 * Sample transaction processor function.
 * @param {org.acme.howto.ChangeStateToTesting} tx The transaction that changes the state of the order from to the testing state.
 * @transaction
 */

function ChangeStateToTesting(tx) {

tx.order.state = "testing";
  
    // Get the asset registry for the order asset.
    return getAssetRegistry('org.acme.howto.Order')
        .then(function (assetRegistry) {

            // Update the asset in the order asset registry.
            return assetRegistry.update(tx.order);
        });
}

/**
 * Sample transaction processor function.
 * @param {org.acme.howto.ChangeStateToDeployment} tx The transaction that changes the state of the order from to the deployment state.
 * @transaction
 */

function ChangeStateToDeployment(tx) {

tx.order.state = "deployment";
  
    // Get the asset registry for the order asset.
    return getAssetRegistry('org.acme.howto.Order')
        .then(function (assetRegistry) {

            // Update the asset in the order asset registry.
            return assetRegistry.update(tx.order);
        });
}

/**
 * Sample transaction processor function.
 * @param {org.acme.howto.ChangeOwner} tx The transaction that changes the owner of the order (i.e. from Company to Engineer).
 * @transaction
 */

function ChangeOwner(tx) {

  tx.order.owner = tx.newOwner;
  
    // Get the asset registry for the order asset.
    return getAssetRegistry('org.acme.howto.Order')
        .then(function (assetRegistry) {

            // Update the asset in the order asset registry.
            return assetRegistry.update(tx.order);
        });
}