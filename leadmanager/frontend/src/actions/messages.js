import { CREATE_MESSAGE } from './types';

export const creatMessage = msg => {
    return {
        type: CREATE_MESSAGE,
        payload: msg
    }
}